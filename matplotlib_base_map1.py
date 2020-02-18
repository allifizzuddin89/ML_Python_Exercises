#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#Base map
#download basemap at https://github.com/matplotlib/basemap/releases/
#or unofficial link at https://www.lfd.uci.edu/~gohlke/pythonlibs/ ;find 'basemap'

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#Call basemap
#other projection option check at https://matplotlib.org/basemap/users/mapsetup.html 
m = Basemap(projection='mill')
#min to show up map
m.drawcoastlines()
#can fill the color later
m.fillcontinents()

plt.title('Basemap Basic')
plt.show()