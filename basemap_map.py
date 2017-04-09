from mpl_toolkits.basemap import Basemap 
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
import matplotlib.cm as cm

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


