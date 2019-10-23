#read files

manu0 = 'ssa_urop_maneuver_10000.txt'
manu1 = 'ssa_urop_maneuver_10001.txt'
manu2 = 'ssa_urop_maneuver_10002.txt'
manu3 = 'ssa_urop_maneuver_10003.txt'
manu4 = 'ssa_urop_maneuver_10004.txt'
manu5 = 'ssa_urop_maneuver_10005.txt'
manu6 = 'ssa_urop_maneuver_10006.txt'

def organize_data(manu):
    with open(manu) as f:
        lines = f.read().splitlines()
        print(lines[2])
        for index in range(0, len(lines)):
            lines[index] = lines[index].split(" ")
    return lines

#manus list is all maneuvers --> one manuever --> one line ---> column item
manus = []
manus.append(organize_data(manu0))
manus.append(organize_data(manu1))
manus.append(organize_data(manu2))
manus.append(organize_data(manu3))
manus.append(organize_data(manu4))
manus.append(organize_data(manu5))
manus.append(organize_data(manu6))

#starting time
#determine where the orbits diverge

def divergence(manu):
    for a in range(0, len(manus[1])):
        #if percent error is larger than 5%, the maneuver must have begun
        try:
            if abs((float(manus[manu][a][7]) - float(manus[0][a][8]))/float(manus[0][a][7])) > 0.05:
                return a
                #return str(manus[manu][a][1], manus[manu][a][2], manus[manu][a][3], manus[manu][a][4], manus[manu][a][5], manus[manu][a][6])
        except:
            if abs((float(manus[manu][a][7]) - float(manus[0][a][8]))/0.001) > 0.05:
                return a

print("Manuever Starting Times")
starting_time_indexes = []
for b in range(1, 6):
    starting_time_indexes.append(divergence(b))
    a = starting_time_indexes[b-1]
    print("Manuever", b, str(manus[b][a][1]), str(manus[b][a][2]), str(manus[b][a][3]), str(manus[b][a][4]), str(manus[b][a][5]), str(manus[b][a][6]))

#ending time
#determine where the maneuver ends by seeing when acceleration is 0 (velocity remains constant)

def constant_velocity(manu):
    for a in range(1, len(manus[1])):
        #velocities are in columns 10-12
        speed1 = (float(manus[manu][a-1][10])**2 + float(manus[manu][a-1][11])**2 + float(manus[manu][a-1][12])**2)**0.5
        speed2 = (float(manus[manu][a][10])**2 + float(manus[manu][a][11])**2 + float(manus[manu][a][12])**2)**0.5
        #speed1 = (manus[manu][a-1][10]**2 + manus[manu][a-1][11]**2 + manus[manu][a-1][12]**2)**0.5
        #speed2 = (manus[manu][a][10]**2 + manus[manu][a][11]**2 + manus[manu][a][12]**2)**0.5
        #epochs are 10 minutes apart
        if (speed2-speed1)/10 < 0.05:
            return a
            #return str(manus[manu][a][1], manus[manu][a][2], manus[manu][a][3], manus[manu][a][4], manus[manu][a][5], manus[manu][a][6])

print("Manuever Ending Times")
ending_time_indexes = []
for b in range(1, 6):
    ending_time_indexes.append(constant_velocity(b))
    a = ending_time_indexes[b-1]
    print("Manuever", b, str(manus[b][a][1]), str(manus[b][a][2]), str(manus[b][a][3]), str(manus[b][a][4]), str(manus[b][a][5]), str(manus[b][a][6]))

#magnitude
def magnitude(start, stop, manu):
    #7-9 are (x, y, z)
    return ((float(manus[manu][stop][7])-float(manus[manu][start][7]))**2 +(float(manus[manu][stop][8])-float(manus[manu][start][8]))**2 +(float(manus[manu][stop][9])-float(manus[manu][start][9]))**2)**0.5

print("Magnitudes")
for b in range(1, 6):
    print(magnitude(starting_time_indexes[b-1], ending_time_indexes[b-1], b))

#direction
#find directional unit vector by dividing vector by magnitude
def direction(start, stop, manu):
    mag = magnitude(starting_time_indexes[manu-1], ending_time_indexes[manu-1], manu)
    return ((float(manus[manu][stop][7])-float(manus[manu][start][7]))/mag, (float(manus[manu][stop][8])-float(manus[manu][start][8]))/mag, (float(manus[manu][stop][9])-float(manus[manu][start][9]))/mag)

print("Directions")
for b in range(1, 6):
    print(direction(starting_time_indexes[b-1], ending_time_indexes[b-1], b))
