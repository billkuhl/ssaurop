#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:50:57 2019
@author: jordanwilke
"""

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from scipy.cluster.vq import kmeans,vq
import numpy as np
from numpy import vstack, array
from pylab import plot, show
import matplotlib.pyplot as plt
import getdata

def iter_clusters(x,y):
	

	

	distortion = []
	iterations = range(1, 10)

	for p in iterations:
	    kmeans_model = KMeans(n_clusters=p).fit(x)
	    distortion.append(sum(np.min(cdist(x, kmeans_model.cluster_centers_, 'euclidean'), axis=1) / x.shape[0]))

	plt.style.use('seaborn')
	fig, ax = plt.subplots(num=1, nrows=1, ncols=1, clear=True)
	fig.suptitle("Elbow Plot for Iris dataset for k-means")
	ax.plot(iterations, distortion, marker='o', linestyle="--")
	ax.set_xlabel("k (Number of centroids)")
	ax.set_ylabel("Distortion (Mean Euclidean distances)")
	plt.show()

	kmeans_model = KMeans(n_clusters=2, random_state=1).fit(x)
	predict = kmeans_model.labels_

	#print(accuracy_score(y, predict))
	#print(f1_score(y, predict, average=None))

def cluster(x,y,n):
	# data generation
	kmeans = KMeans(n_clusters=n)
	kmeans.fit(x)
	y_kmeans = kmeans.predict(x)
	plt.scatter(x[:,0], y[:,0], c=y_kmeans, s=50, cmap='viridis')
	plt.show()
	centers = kmeans.cluster_centers_
	print(centers)
	plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
	plt.show()

if __name__ == '__main__':
	data_bunch = getdata.wk1
	


	x = data_bunch.NORAD_CAT_ID.values
	y = data_bunch.ECCENTRICITY.values
	x = np.reshape(x,(-1,1))
	y = np.reshape(y,(-1,1))

	cluster(x,y,4)

	'''

	So this was a different attempt to get it to work, not sure how well it went 

	'''

	'''
	X = []
	Y = []
	for i in range(len(data_bunch.EPOCH.values)):
		X.append([data_bunch.EPOCH.values[i],data_bunch.ECCENTRICITY.values[i]])
		Y.append(data_bunch.NORAD_CAT_ID.values[i])

	X = np.reshape(X,(-1,1))
	Y = np.reshape(Y,(-1,1))
	print(X)
	cluster(X,Y,4)
	'''














