#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#subplot

import matplotlib.pyplot as plt 
import random
from matplotlib import style 

#plot style, font, width etc..
style.use('fivethirtyeight')

fig = plt.figure()

def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs,ys

'''
#create subplot
#2 by 1 subplot

ax1 = fig.add_subplot(211) #(2 by 1, subplot 1)
ax2 = fig.add_subplot(212) #(2 by 1, subplot 2)

#call create_plot ftn for each subplot
#xs and ys is returned to x,y
x,y = create_plots()
ax1.plot(x,y)

x,y = create_plots()
ax2.plot(x,y)
'''

'''
#create 3 subplot
#221,222,212 is the biggest subplot
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)
'''

#better way to use subplot
#use subplot2grid
#we can manage how much row and column we want to occupy for each subplot
#subplot2grid((row,col),(startrow,startcol),rowspan=total row, colspan=totalcol)
ax1 = plt.subplot2grid((6,1),(0,0), rowspan=2, colspan=1)
ax2 = plt.subplot2grid((6,1),(2,0), rowspan=2, colspan=1)
ax3 = plt.subplot2grid((6,1),(4,0), rowspan=2, colspan=1)

x,y = create_plots()
ax1.plot(x,y)

x,y = create_plots()
ax2.plot(x,y)

x,y = create_plots()
ax3.plot(x,y)

plt.show()