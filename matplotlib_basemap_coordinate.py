#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#Basemap coordinate

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 

#Locate JB and Puncak Alam
#draw line connect both
#draw arc line

#create list to create connecting line
xs = []
ys = []

#lets make projection of Malaysia map
m = Basemap(projection='mill',llcrnrlat=-10 ,llcrnrlon=90 , urcrnrlat=20 , urcrnrlon=130, resolution='h')
m.drawcoastlines()
m.drawcounties(linewidth=2)
m.drawstates(color='b')
#m.etopo()
m.bluemarble()

#lets find Puncak Alam, Selangor, Malaysia
#use coordinate 3.23648,101.425
PAMylat, PAMyLon = 3.23648,101.425
xpt, ypt = m(PAMyLon,PAMylat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt,ypt,'c*',markersize=15) #m.plot(lon,lat,color and marker(cyan circle),markersize)

#Johor Bahru, Johor, Malaysia lat = 1.4953, lon = 103.755 
JBlat, JBlon = 1.4953, 103.755
xpt, ypt = m(JBlon, JBlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt,ypt, 'r^', markersize=15)

#plot line
m.plot(xs,ys, linewidth=3, color='black', label= 'Travel Line')

#create arc line
#got issue, it does not curve
#refer doc, it cannot draw to edge of the map
#m.drawgreatcircle(PAMyLon,PAMylat,JBlon,JBlat, del_s=500 ,color='y', linewidth=3, label='Arc')

plt.legend(loc=4) #rearrange label location
plt.title('Malaysia Map')
plt.show()
plt.close()