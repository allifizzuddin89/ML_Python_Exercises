#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#LIVE Graph
#could pickup real time data
#stock
#sensors

import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#could open any data log or json or api
#for example we create a dummy sensor file
def animate(i):
    graph_data = open('sensor_data.txt','r').read()
    lines = graph_data.split('\n')#line by line in the text file
    xs = []
    ys = []
    for line in lines:
        if len(line)>1:
            x,y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs,ys)

#update animation every 1000ms
ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()