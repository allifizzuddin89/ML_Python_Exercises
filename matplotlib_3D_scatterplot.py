#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#3D chart
#scatter plot

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')

x = [1,2,3,4,5,6,7,8,9,10]
y = [11,12,13,14,15,16,17,18,19,20]
z = [21,22,23,24,25,26,27,28,29,30]

x1 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y1 = [-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]
z1 = [-21,-22,-23,-24,-25,-26,-27,-28,-29,-30]

ax1.scatter(x,y,z, c='b', marker='o')
ax1.scatter(x1,y1,z1, c='y', marker='*')

ax1.set_xlabel('X-Axis')
ax1.set_ylabel('Y-Axis')
ax1.set_zlabel('Z-Axis')

plt.show()