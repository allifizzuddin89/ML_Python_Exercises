#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#3D chart
#basic

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()

#create sublot 1 by 1 and its location is in subplot 1
ax1 = fig.add_subplot(111,projection='3d') 

x = [1,2,3,4,5,6,7,8,9,10]
y = [11,12,13,14,15,16,17,18,19,20]
z = [21,22,23,24,25,26,27,28,29,30]

#ax1.plot_wireframe(x,y,z) #not working since this is not a wireframe
ax1.plot(x,y,z)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

#plt.legend(loc=4)
plt.show()