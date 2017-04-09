import string
from datetime import datetime
from collections import Counter
import codecs
from mpl_toolkits.basemap import Basemap 
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
import matplotlib.cm as cm


filename = 'problem2.txt'

with open(filename) as f:
    events = f.readlines()

# for x in range(len(events)):
#     events[x] = events[x].split(";")


for x in range(len(events)):
    events[x] = events[x].split(";")
    date_time, identity, cell = events[x]
    year = date_time[0:4]
    month = date_time[5:7]
    day = date_time[8:10]
    time = date_time[11:19]
    events[x] = [date_time, year, month, day, time, identity, cell, 0]


def function_datetime(date_str):
    return datetime.strptime(date_str[0:19], "%Y-%m-%dT%H:%M:%S")


identity_list = []
for event in events:
    identity_list.append(event[5])

identity_list = list(set(identity_list))
     
#events = sorted(events, key=lambda e: (e[5], e[0]))
events.sort(key=lambda e: (e[5], e[0]))

def calculate_delta(event_now, event_next):
    return (function_datetime(event_next)-function_datetime(event_now)).total_seconds() 

for person in identity_list:
    for i in range(1,len(events)):
        if events[i-1][5]==person and events[i][5]==person:
            events[i-1][7] = calculate_delta(events[i-1][0], events[i][0])

cells_identity_list = []
cells_list = []
for event in events:
    if event[7]>=3600:
        cells_identity_list.append([event[5], event[6]])
        cells_list.append(event[6])


d = Counter(cells_list)
print(d)


#------PART 2: GPS Coordinates------------#
#-----------------------------------------#


filename_coord = 'lac_locations.txt'

with codecs.open(filename_coord, encoding='utf-16') as f:
    lacs = f.readlines()

for x in range(len(lacs)):
    lacs[x] = lacs[x].split(";")


full_lacs = []

for k,v in d.items():
    for lac in lacs:
        if k[0:3]==lac[0]:
            full_lacs.append([k, v, lac[1], lac[2]])

print(full_lacs)

#-----------------PART 3-------------#
#------------------------------------#


 
x=[] #longitudes
y=[] #latitudes

# linenum=0
# for line in fi:
#     if linenum>0:
#         line=string.replace(line, "\n","")
#         try:
#             fields=string.split(line,",")
#             lon,lat=fields[0:2]
#             x.append(float(lon))
#             y.append(float(lat))
#         except:
#             pass
#     linenum+=1
# fi.close()

for lac in full_lacs:
    x.append(lac[2][0:9])
    y.append(lac[3][0:9])


x = [float(i) for i in x]
y = [float(i) for i in y]

print(x)

plt.figure(figsize=(30,35))
map = Basemap(width=28,height=33,projection='mill', lat_0=38.0, lon_0=-9.0, llcrnrlon=-9.5000,
    llcrnrlat=37.0100,urcrnrlon=-6.1900,urcrnrlat=42.1500, epsg=3763, resolution='l')


# map.drawmapboundary(fill_color='aqua')
# map.drawcountries()
# map.fillcontinents(color='coral',lake_color='aqua')
# map.drawcoastlines()

lons = [-8.6291, -9.1393]
lats = [41.1579, 38.7223]
x,y = map(lons, lats)
labels=[1000, 4000]

#map.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 1500, verbose= True)
map.arcgisimage(service='World_Street_Map', xpixels = 1500, verbose= True)
# plt.annotate("Lisboa", xy = (x[1],y[1])) 
# plt.annotate("Porto", xy = (x[0],y[0])) 
# plt.plot(x, y, 'bo', markersize=14, color='red')

# plt.show()
plt.scatter(x,y,s=labels)
plt.show()


