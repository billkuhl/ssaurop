# using the ECEF standard for positions.
import sys
import ephem
import math




#ephem.separation((lon1, lat1), (lon2, lat2))
sattle1 = '25473.txt'
sattle2 = '26824.txt'
sattle3 = '27438.txt'
sattle4 = '39509.txt'
sattle5 = '40258.txt'

def create_history(sat):
	history = []
	with open(sat) as f:
		lines = f.read().splitlines()
	#print (lines[::10])
		
	for line in range(0,len(lines),2):

		#print(line,line+1,sat[line],sat[line+1])
		inst = ephem.readtle('sat',lines[line],lines[line+1])
		print(inst)
		history.append(inst)
		
	#print('history',history)
	return history

sat1 = (create_history(sattle1))
sat2 = (create_history(sattle2))
sat3 = (create_history(sattle3))
sat4 = (create_history(sattle4))
sat5 = (create_history(sattle5))
sats = [sat1,sat2,sat3,sat4,sat5]


	
def find_dist(s1,s2):
	s1.compute()
	s2.compute()
	lat = (s1.sublat)
	lon = (s1.sublong)
	alt = (s1.elevation)

	x_1 = alt * math.cos(lat) * math.sin(lon)
	y_1 = alt * math.sin(lat)
	z_1 = alt * math.cos(lat) * math.cos(lon)

	lat = (s2.sublat)
	lon = (s2.sublong)
	alt = (s2.elevation)

	x_2 = alt * math.cos(lat) * math.sin(lon)
	y_2 = alt * math.sin(lat)
	z_2 = alt * math.cos(lat) * math.cos(lon)
	
	return ((x_2-x_1)**2 + (y_2-y_1)**2 + (z_2-z_1)**2)**(1/2)
print(find_dist(sat1[0],sat2[0]))



