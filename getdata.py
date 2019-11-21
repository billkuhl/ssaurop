import pandas as pd 
from datetime import datetime

wk1 = pd.read_csv(r'AstroYWeek1DataSet.csv')
wk2 = pd.read_csv(r'AstroYWeek2DataSet(Corrected).csv')
newtimes = []
newtimes2 = []
for item in wk1['EPOCH']:
	datetime_object = datetime.strptime(item,'%Y-%m-%d %X')
	ts = datetime_object.timestamp()
	newtimes.append(ts)
wk1['EPOCH'] = newtimes

for item in wk2['EPOCH']:
	datetime_object = datetime.strptime(item,'%Y-%m-%d %X')
	ts = datetime_object.timestamp()
	newtimes2.append(ts)
wk2['EPOCH'] = newtimes2

satdict = {}
satdict2 = {}
for row in wk1.values.tolist():
	if row[0] in satdict.keys():
		satdict[row[0]].append(row[1:])
	else:
		satdict[row[0]] = [row[1:]]

for row in wk2.values.tolist():
	if row[0] in satdict2.keys():
		satdict2[row[0]].append(row[1:])
	else:
		satdict2[row[0]] = [row[1:]]

print(len(satdict))
print(len(satdict2))
unique = []
for key in satdict.keys():
    if key not in satdict2.keys():
        unique.append(key)
print(len(unique))
def get_sat_ids():
	sat_ids = set()
	for item in wk1['NORAD_CAT_ID']:
		if item not in set():
			sat_ids.add(item)

def get_specific_data(sat,feature):
	featdict = {'EPOCH':0,'MEAN_MOTION':1,'ECCENTRICITY':2,'INCLINATION':3,'RA_OF_ASC_NODE':4,'ARG_OF_PERICENTER':5,'MEAN_ANOMALY':6,'SEMIMAJOR_AXIS':7,'PERIOD':8, 'APOGEE':9,'PERIGEE':10}
	s = satdict[sat]
	d = []
	for line in s:
		d.append([line[featdict[feature]]])
	return d

def convert_date_to_epoch(date):
    epoch = date[2:4]
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    month = date[5:7]
    total = 0
    for i in range(1,int(month)):
        total+= months[i]
    total += int(date[8:10])
    hours = date[11:13]
    minutes = date[14:16]
    minutesInADay = 24*60
    decimal = (int(hours)*60 + int(minutes))/minutesInADay
    decimal = str(decimal)
    return epoch + str(total) + decimal[1:]



if __name__ == '__main__':
    print(get_specific_data(9191,'PERIGEE'))
    print(get_specific_data(11682,'PERIGEE'))
    print(get_specific_data(30206,'PERIGEE'))
    print(get_specific_data(79815,'PERIGEE'))
    print(get_specific_data(74415,'PERIGEE'))
	#print(get_specific_data(1194, "MEAN_MOTION"))
	#print(satdict[1194])


