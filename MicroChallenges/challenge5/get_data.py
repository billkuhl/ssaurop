'''
Created 11/6/2019
Bill Kuhl

This contains a bunch of functions for taking in things from STK and returning the fixed data
'''
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from scipy.spatial.distance import cdist
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt


def getdata(file):
    with open(file) as f:
        rawdata = f.readlines()
    dataset = []
    total = []
    for line in rawdata:
        newline = line.rstrip('\r\n')
        newline = newline.split()
        if len(newline) == 2 and '--------------------' not in newline:
            dataset.append([newline[0],newline[1]])

    
    return dataset

def KMeansTest(sats):
    
    data = []
    for sat in sats:
        elements = []
        for i in range(len(sats[0])):
            elements.append(sat[i][0])
        data.append(sat)
    print(sats[0][0])
    distortion = [] 
    iterations = range(1,6)
    
    #Creates the graph to see how many clusters to use. Probably should use 2
    #for p in iterations:
    #    kmeans_model = KMeans(n_clusters=p, random_state=1).fit(sat)
    #    distortion.append(sum(np.min(cdist(sat,kmeans_model.cluster_centers_,'euclidean'), axis=1)/len(sat)))
    #    print(p)
    
    
    #plt.style.use('seaborn')
    #fig, ax = plt.subplots(num=1,nrows=1,ncols=1,clear=True)
    #fig.suptitle("Elbow Plot for Iris dataset for k-means")
    #ax.plot(iterations, distortion, marker='o', linestyle="--")
    #ax.set_xlabel("k (Number of centroids)")
    #ax.set_ylabel("Distortion (Mean Euclidean distances)")
    
    kmeans_model = KMeans(n_clusters=2, random_state=1).fit(sat)
    print(kmeans_model.cluster_centers_)
    #print(accuracy_score(y, predict))
    #print(f1_score(y,predict,average=None))

sat22927 = getdata("22927.txt")
sat24812 = getdata("24812.txt")
sat36516 = getdata("36516.txt")
sat37392 = getdata("37392.txt")
sat39122 = getdata("39122.txt")

#sat39476 = getdata("39476.txt")
#sat40424 = getdata("40424.txt")
#sat40425 = getdata("40425.txt")
#sat40875 = getdata("40875.txt")
#sat41308 = getdata("41308.txt")
#Add the other satellite files and add the objects to the array
sats = [sat22927,sat24812,sat36516,sat37392,sat39122]
KMeansTest(sats)
