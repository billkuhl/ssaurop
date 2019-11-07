'''
Created 11/6/2019
Bill Kuhl

This contains a bunch of functions for taking in things from STK and returning the fixed data
'''
import pandas as pd

def getdata(file):
    with open(file) as f:
        rawdata = f.readlines()
    dataset = {'inclination':[],'semi_major_axis':[]}
    total = []
    for line in rawdata:
        newline = line.rstrip('\r\n')
        newline = newline.split()
        if len(newline) == 2 and '--------------------' not in newline:
            dataset['inclination'].append(newline[1])
            dataset['semi_major_axis'].append(newline[0])

    df = pd.DataFrame(dataset)
    return df



file = './data/Telstar401_22927_inc_semi-maj-axis.txt'
print(getdata(file))