from __future__ import absolute_import, division, print_function, unicode_literals

import pathlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)

def import_data():
	titles = ['COMMENT','ORIGINATOR','NORAD_CAT_ID','OBJECT_NAME','OBJECT_TYPE','CLASSIFICATION_TYPE','INTLDES','EPOCH','EPOCH_MICROSECONDS','MEAN_MOTION','ECCENTRICITY','INCLINATION','RA_OF_ASC_NODE','ARG_OF_PERICENTER','MEAN_ANOMALY','EPHEMERIS_TYPE','ELEMENT_SET_NO','REV_AT_EPOCH','BSTAR','MEAN_MOTION_DOT','MEAN_MOTION_DDOT','FILE','TLE_LINE0','TLE_LINE1','TLE_LINE2','OBJECT_ID','OBJECT_NUMBER','SEMIMAJOR_AXIS','PERIOD','APOGEE','PERIGEE']
	data_dict = {}
	for item in titles:
		data_dict[item] = []
#GENERATED VIA SPACETRACK.ORG API,18 SPCS,41616,FLOCK 2P 5,PAYLOAD,U,16040T,5/11/2018 19:56,294304,15.24284132,0.0010712,97.4199,197.0357,19.7074,340.4576,0,999,10468,6.74E-05,1.58E-05,0,2283918,0 FLOCK 2P 5,1 41616U 16040T   18131.83058211  .00001576  00000-0  67370-4 0  9997,2 41616  97.4199 197.0357 0010712  19.7074 340.4576 15.24284132104680,2016-040T,41616,6871.072,94.47,500.298,485.577
	data = open('planet.txt','r+')
	data = data.readlines()
	for line in data:
		splitline = line.split(',')
		for i in range(len(splitline)):
			data_dict[titles[i]].append(splitline[i])
	data_dict['FILLER'] = [i for i in range(len(data))]

	return {'BSTAR':data_dict['BSTAR'],'EPOCH':data_dict['EPOCH']}



#This is what a timestamp looks like
#5/13/2018 16:02

#finds number of days in a month
def month_num_days(month, year):
    if (month % 2 == 1):
        return 31
    if(month % 2 == 0 and not month == 2):
        return 30
    if (month == 2):
        if (year % 4 == 0):
            return 29
        else:
            return 28

def days_in_months(month, year):
    days = 0
    for i in range(1, month+1):
        days += month_num_days(i, year)
    return days

def year_num_days(year):
    if (year % 4 == 0):
        return 357
    else:
        return 356

#turns timestamp into minutes since the first minute of the first timestamp's year
def epoch_to_minutes(first_year, num):
    num_array = num.split(" ")
    month_day_year = num_array[0].split("/")
    hour_minute = num_array[1].split(":")
    for i in range(0, len(month_day_year)):
        month_day_year[i] = int(month_day_year[i])
    for i in range(0, len(hour_minute)):
        hour_minute[i] = int(hour_minute[i])
    minutes = 0
    #add minutes
    minutes += hour_minute[1]
    #add hours
    minutes += hour_minute[0]*60
    #add days
    minutes += month_day_year[1]*60*24
    #add months
    months = month_day_year[0]
    years = month_day_year[2]
    minutes += days_in_months(months, years)*60*24
    #add years
    minutes += (years - first_year)*60*24*year_num_days(years)
    return minutes

#turns the epoch array into an array of minutes since the first minute of the first timestamp's year
def process_nums(epoch_array):
    num = epoch_array[0]
    num_array = num.split(" ")
    month_day_year = num_array[0].split("/")
    first_year = int(month_day_year[2])
    first_minutes = epoch_to_minutes(first_year, epoch_array[0])
    epoch_in_minutes = []
    for i in epoch_array:
        epoch_in_minutes.append(epoch_to_minutes(first_year, i)-first_minutes)
    return epoch_in_minutes

# fake_epochs = ["5/13/2018 16:02", "5/14/2018 13:48", "1/4/2019 4:34"]
# print(process_nums(fake_epochs))








data = import_data()
newbstar = []
for item in data['BSTAR']:
	newbstar.append(float(item))
data['BSTAR'] = newbstar

newepoch = process_nums(data['EPOCH'])
data['EPOCH'] = newepoch
df = pd.DataFrame(data)
print(df.dtypes)


train_dataset = df.sample(frac=0.8,random_state=0)
test_dataset = df.drop(train_dataset.index)

train_labels = train_dataset.pop('BSTAR')
test_labels = test_dataset.pop('BSTAR')




def build_model():
  model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
  ])

  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model

model = build_model()
model.summary()

example_batch = train_dataset[:10]
example_result = model.predict(example_batch)

class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

EPOCHS = 1000

history = model.fit(
  train_dataset, train_labels,
  epochs=EPOCHS, validation_split = 0.2, verbose=0,
  callbacks=[PrintDot()])

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
(hist.tail())

def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch

  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error')
  plt.plot(hist['epoch'], hist['mae'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mae'],
           label = 'Val Error')
  plt.ylim([0,1000])
  plt.legend()

  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error')
  plt.plot(hist['epoch'], hist['mse'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mse'],
           label = 'Val Error')
  plt.ylim([0,2000])
  plt.legend()
  #plt.show()


plot_history(history)

model = build_model()

# The patience parameter is the amount of epochs to check for improvement
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

history = model.fit(train_dataset, train_labels, epochs=EPOCHS,
                    validation_split = 0.2, verbose=0, callbacks=[early_stop, PrintDot()])

(plot_history(history))

test_predictions = model.predict(test_dataset).flatten()

plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.axis('equal')
plt.axis('square')
plt.xlim([0,plt.xlim()[1]])
plt.ylim([0,plt.ylim()[1]])
_ = plt.plot([-1000, 1000], [-1000, 1000])
plt.show()

'''
ok, so it does train and run this data, but I could use some help to figure out how to
make this more accurate to the data.  I didnt bother trying to fit this to the TLE data
until I get this with a tight tolerance, otherwise I would just be doing something wrong
more than once.  Any help to figure out how to make this better would  be greatly appreciated.

'''
