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

'''
x = [1,2,3,4,5,6,7,8,9,10]
y = [11,12,13,14,15,16,17,18,19,20]
z = [21,22,23,24,25,26,27,28,29,30]

x1 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y1 = [-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]
z1 = [-21,-22,-23,-24,-25,-26,-27,-28,-29,-30]
'''

x3 = [1,2,3,4,5,6,7,8,9,10]
y3 = [11,12,13,14,15,16,17,18,19,20]
z3 = np.zeros(10) #actually we only plot x and y by letting z to zero

#introduce another dimension for starting point on z
dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,3,4,5,6,7,8,9,10]

ax1.bar3d(x3,y3,z3, dx,dy,dz)
ax1.set_xlabel('X-Axis')
ax1.set_ylabel('Y-Axis')
ax1.set_zlabel('Z-Axis')

plt.show()