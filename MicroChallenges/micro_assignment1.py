class sat:
    def __init__(self,line1,line2):
        self.sat_num = line2[1]
        self.classification = line1[1][-1]
        self.international_designator = line1[2]
        self.epoch = line1[3]
        self.time_deriv_mean_motion1 = line1[4]
        self.time_deriv_mean_motion2 = line1[5]
        self.drag_term = line1[6]
        self.emphemeris_type = line1[7]
        self.element_num = line1[8]
        self.inclination = line2[2]
        self.right_asc_node = line2[3]
        self.eccentricity = line2[4]
        self.argument_pedigree = line2[5]
        self.mean_anomoly = line2[6]
        self.neam_motion = line2[7]
        #self.revolution_num_epoch = line2[8]
        self.apogee = ((((6.67430e-11)*(5.9722e24)*(86400**2))/(4*(3.14159**2)*((float(self.neam_motion))**2)))**(1/3))-6378e3
        

    def __str__(self,):
        print('Satellite catalog number:',self.sat_num)
        #print('clasification', self.classification)
        #print('international designator', self.international_designator)
        #print('epoch', self.epoch)
        #print('time derivative of mean motion 1',self.time_deriv_mean_motion1)
        #print('time derivative of mean motion 2',self.time_deriv_mean_motion2)
        #print('drag term', self.drag_term)
        #print('emphemeris type', self.emphemeris_type)
        #print('element number', self.element_num)
        print('Eccentricity (e): 0.' + self.eccentricity)
        print('Mean anomaly (M): ',self.mean_anomoly + '˚')
        print('Right ascension of the ascending node (Ω):',self.right_asc_node + '˚')
        print('Argument of periapsis (ω): ',self.argument_pedigree + '˚')
        print('Inclination (i):', self.inclination + '˚')
        print('Average distance (a):', self.apogee )
        print('mean mootion : ', self.neam_motion)
        
        if self.apogee >= 35800e3:
            print('Orbital: HEO')
        elif self.apogee < 35800e3 and self.apogee > 2000e3:
            if self.apogee < 35886e3 and self.apogee > 35686e3:
                print('Orbital: GEO')
            else:  
                print('Orbital: MEO')
        else:
            print('Orbital: LEO')
            
        return ''
        #print('revolution of number epoch : ',self.revolution_num_epoch)


#Import the text file:
tle1 = open('tle1.txt','r+')

#puts each line into a list of strings
tle_str = tle1.readlines()
tle_list = []

#makes tle_list into a list of lists, made of individual lines with component parts inside them
for item in tle_str:
    ind_tle = item.split(' ')

    #gets rid of the \n term
    hold = ind_tle[-1].split('\n')
    ind_tle.pop()
    for item in hold:
        ind_tle.append(item)
    while '' in ind_tle:
        ind_tle.remove('')
    tle_list.append(ind_tle)

def create_satlist(L):
    final = set()
    for step in range(0,len(tle_list)-1,2):
        new = sat(L[step],L[step+1])
        final.add(new)
    return final


satellites = create_satlist(tle_list)
for item in satellites:
    print(item)



