#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#Base map2

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 


#lat is y-axis, longitude is x-axis
#range of lat and lon as follows:
#llcrnrlat means lowerleft corner latitude
#llcrnrlon menas lower left corner longitude
#urcrnrlat is uppercorner lat
#urcrnrlon is uppercorner lon
#we find Africa
m = Basemap(projection='mill',
llcrnrlat=-40, #40 south
llcrnrlon=-40, #40 west
urcrnrlat=50, #50 north
urcrnrlon=75, #75 east
resolution='f') #c=crude, l=low, h=high, f=full

'''
#WorldMap
m = Basemap(projection='mill',
llcrnrlat=-90, 
llcrnrlon=-180, 
urcrnrlat=90, 
urcrnrlon=180, 
resolution='l') #c=crude, l=low, h=high, f=full
'''

m.drawcoastlines()
m.drawcountries(linewidth=2)
# m.drawstates(color='b')
# m.drawcounties(color='r')
# m.etopo()
# m.bluemarble()
#m.drawcontinents()

plt.title('Basemap Country')
plt.show() 