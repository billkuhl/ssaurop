# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sklearn
import csv
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier



name = []
orbit_class = []
orbit_type = []
perigee = []
apogee = []
eccentricity = []
inclination = []
period = []



def load_data_orbital_class():
    with open('Week2_Problem2.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data_list = []
        data = {"feature_names": ["perigee", "apogee", "eccentricity",
                "inclination", "period"]}
        count = 0
        data_dict = {}
        names = []
        temp_list_labels = []
        for row in csv_reader:
            if line_count > 0:
                
                #data_list["name"] = row[0]
                temp_list = [float(row[10].replace(",","")),float(row[11].replace(",","")),float(row[12].replace(",","")),float(row[13].replace(",","")),float(row[14].replace(",",""))]
                data_list.append(temp_list)
                if row[7] not in data_dict:
                    names.append(row[7])
                    data_dict[row[7]] = count 
                    count +=1
                temp_list_labels.append(data_dict[row[7]])
                line_count += 1
            line_count += 1
        data["data"] = data_list
        data["target"] = temp_list_labels
        data["target_names"] = names
    return data

def load_data_orbital_types():
    with open('Week2_Problem2.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data_list = []
        data = {"feature_names": ["perigee", "apogee", "eccentricity",
                "inclination", "period"]}
        count = 0
        data_dict = {}
        names = []
        temp_list_labels = []
        for row in csv_reader:
            if line_count > 0:
                
                #data_list["name"] = row[0]
                temp_list = [float(row[10].replace(",","")),float(row[11].replace(",","")),float(row[12].replace(",","")),float(row[13].replace(",","")),float(row[14].replace(",",""))]
                data_list.append(temp_list)
                if row[8] not in data_dict:
                    names.append(row[8])
                    data_dict[row[8]] = count 
                    count +=1
                temp_list_labels.append(data_dict[row[8]])
                #data_list["orbit_type"] = row[8]
                #data_list["perigee"] = row[10]
                #data_list["apogee"] = row[11]
                #data_list["eccentricity"] = row[12]
                #data_list["inclination"] = row[13]
                #data_list["period"] = row[14]
                line_count += 1
            line_count += 1
        data["data"] = data_list
        data["target"] = temp_list_labels
        data["target_names"] = names
    return data

def fitGNBModel(data):
    # Load dataset
    label_names = data['target_names']
    labels = data['target']
    feature_names = data['feature_names']
    features = data['data']


    # Split our data
    train, test, train_labels, test_labels = train_test_split(features,
                                                          labels,
                                                          test_size=0.33)

    # Initialize our classifier
    gnb = GaussianNB()
    # Train our classifie
    model = gnb.fit(train, train_labels)
    preds = gnb.predict(test)
    # Evaluate accuracy
    return(accuracy_score(test_labels, preds))

def fitLogisticRegress(data):
    # Load dataset
    label_names = data['target_names']
    labels = data['target']
    feature_names = data['feature_names']
    features = data['data']

    
    
    # Split our data
    train, test, train_labels, test_labels = train_test_split(features,
                                                          labels,
                                                          test_size=0.33)
    
    clf = LogisticRegression(random_state=0, solver='liblinear',
                             multi_class='ovr').fit(train, train_labels)
    preds = clf.predict(test)
    
    # Evaluate accuracy
    return(accuracy_score(test_labels, preds))
    
    
def fitKNearestNeighbor(data):
    # Load dataset
    label_names = data['target_names']
    labels = data['target']
    feature_names = data['feature_names']
    features = data['data']

    
    
    # Split our data
    train, test, train_labels, test_labels = train_test_split(features,
                                                          labels,
                                                          test_size=0.33)
    
    neigh = KNeighborsClassifier()
    neigh.fit(train, train_labels)
    preds = neigh.predict(test)
    
    # Evaluate accuracy
    return(accuracy_score(test_labels, preds))
    

orbital_class_data = load_data_orbital_class()
orbital_type_data = load_data_orbital_types()

def averageOver100Attempts(data, func, classifier, looking_for):
    total = 0
    for i in range(100):
        total += func(data)
    print("Using " + classifier + " to determine " + looking_for + " yielded a " + str(total/100) + " success rate over 100 tries.")

averageOver100Attempts(orbital_class_data, fitGNBModel, "Gaussian NB", "orbital class")
averageOver100Attempts(orbital_type_data, fitGNBModel, "Gaussian NB", "orbital type")
averageOver100Attempts(orbital_class_data, fitLogisticRegress, "Logistic Regression", "orbital class")
averageOver100Attempts(orbital_type_data, fitLogisticRegress, "Logistic Regression", "orbital type")
averageOver100Attempts(orbital_type_data, fitKNearestNeighbor, "K-Nearest Neighbor", "orbital class")
averageOver100Attempts(orbital_type_data, fitKNearestNeighbor, "K-Nearest Neighbor", "orbital type")
