#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:13:37 2019

@author: jordanwilke
"""

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from scipy.spatial.distance import cdist
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

#from plot_confusion_matrix import plot_confusion_matrix

data_bunch = load_iris()
x=data_bunch.data
y = data_bunch.target

x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.80)

forest_model = RandomForestClassifier(n_estimators=100, criterion="gini", verbose=1)

forest_model.fit(x_train, y_train)

predict = forest_model.predict(x_test)

print(accuracy_score(y_test, predict))
print(confusion_matrix(y_test, predict))
print(f1_score(y_test,predict,average=None))

importances = forest_model.feature_importances_

plt.style.use('seaborn')
fig = plt.figure()
ax = plt.axes()

ax.barh(data_bunch.feature_names, importances)
ax.set_xlabel('Importance')
ax.set_ylabel("Feature")
ax.set_title("Feature Selection with Random Forest Classifier")
plt.tight_layout()