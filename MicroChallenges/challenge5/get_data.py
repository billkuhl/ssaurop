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



files = '22927.txt'
sat22927 = getdata("22927.txt")
#sat24812 = getdata("24812.txt")
#sat36516 = getdata("36516.txt")
#sat37392 = getdata("37392.txt")
#sat39122 = getdata("39122.txt")
#sat39476 = getdata("39476.txt")
#sat40424 = getdata("40424.txt")
#sat40425 = getdata("40425.txt")
#sat40875 = getdata("40875.txt")
#sat41308 = getdata("41308.txt")