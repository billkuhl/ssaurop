import pandas as pd 
from datetime import datetime

wk1 = pd.read_csv(r'AstroYWeek1DataSet.csv')
newtimes = []
for item in wk1['EPOCH']:
	datetime_object = datetime.strptime(item,'%Y-%m-%d %X')
	ts = datetime_object.timestamp()
	newtimes.append(ts)
wk1['EPOCH'] = newtimes
satdict = {}
for row in wk1.values.tolist():
	if row[0] in satdict.keys():
		satdict[row[0]].append(row[1:])
	else:
		satdict[row[0]] = [row[1:]]

def get_sat_ids():
	sat_ids = set()
	for item in wk1['NORAD_CAT_ID']:
		if item not in set():
			sat_ids.add(item)

def get_specific_data(sat,feature):
	featdict = {'EPOCH':0,'MEAN_MOTION':1,'ECCENTRICITY':2,'INCLINATION':3,'RA_OF_ASC_NODE':4,'ARG_OF_PERICENTER':5,'MEAN_ANOMALY':6,'SEMIMAJOR_AXIS':7,'PERIOD':8,'PERIOD':9,'APOGEE':10,'PERIGREE':11}
	s = satdict[sat]
	d = []
	for line in s:
		d.append(line[featdict[feature]])
	return d



if __name__ == '__main__':
	print(get_specific_data(43,'EPOCH'))


