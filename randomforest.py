import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import StandardScalar
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import matplotlib.pyplot as plt

import graphviz
from subprocess import call
from IPython.display import Image

import getdata

dataset = getdata.wk1

X = dataset.iloc[:,0:11]
y = dataset.iloc[:,11]

X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

# sc = StandardScalar()
# X_train = sc.fit_transform(X_train)
# X_test = sc.fit_transform(X_test)

regressor = RandomForestRegressor(n_estimators=20,random_state=0)
regressor.fit(X_train,y_train)
y_pred = regressor.predict(X_test)

print('mean absolute error', metrics.mean_absolute_error(y_test,y_pred))
print('mean squared error', metrics.mean_squared_error(y_test,y_pred))
print('root mean squared error',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

# my attempt to get the thing to work

# estimator = regressor.estimators_[5]

# graphviz(estimator,out_file='tree.dot',feature_names=dataset.columns.values,
# 	class_names=dataset.columns.values,rounded=True,proportion=False,sprecision=2,filled=True)

# call(['dot','-Tpng','tree.dot','-o','tree.png','-Gdpi=600'])

# Image(filemane='tree.png')

importances = regressor.feature_importances_
plt.style.use('seaborn')
fig = plt.figure()
ax = plt.axes()

ax.barh(dataset.columns.values, importances)
ax.set_xlabel('Importance')
ax.set_ylabel("Feature")
ax.set_title("Feature Selection with Random Forest Classifier")
plt.tight_layout()