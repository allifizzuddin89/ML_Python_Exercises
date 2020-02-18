#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#3D chart
#bar chart

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt 
import numpy as np

#add style
from matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

#obtain sample data from axes3d
x,y,z = axes3d.get_test_data()

#we can see where is the axes3d file sample
print(axes3d.__file__)

ax1.plot_wireframe(x,y,z, rstride = 5, cstride = 5) #stride makes gap

ax1.set_xlabel('X-Axis')
ax1.set_ylabel('Y-Axis')
ax1.set_zlabel('Z-Axis')

plt.show()

#can refer doc matlotlib.org/gallery for more graph type
#styudy seaborn for more data visualization