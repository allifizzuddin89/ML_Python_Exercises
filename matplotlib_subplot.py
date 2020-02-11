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
#ax3v = ax3.twinx()
'''
#if want some ax(n) share same x-axis
use sharex=ax(n)
ax3 = plt.subplot2grid((6,1),(4,0),rowspan=2, colspan=1, sharex=ax1)

#if want to have overlap polygon plot e.g volume..etc..
#use twinx() and fill_between
ax3v = ax3.twinx()
#ax3v.fill_between(x-axis data,begin y-axis(opt),y-axis data, facecolor='colorcode',alpha=opaqueness range)
ax3v.fill_between(x,0,y, facecolor='r',alpha=0.4)
'''
x,y = create_plots()
ax1.set_ylabel('Y')
ax1.set_xlabel('X')
ax1.set_title('AX1 Plot')
ax1.plot(x,y,label='Test 1') #customize legend

x,y = create_plots()
ax2.set_ylabel('Y')
ax2.set_xlabel('X')
ax2.set_title('AX2 Plot')
ax2.plot(x,y)

x,y = create_plots()
#ax3v.fill_between(x,0,y, facecolor='r',alpha=0.4)
ax3.set_ylabel('Y')
ax3.set_xlabel('X')
ax3.set_title('AX1 Plot')
ax3.plot(x,y)

#plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.subplots_adjust(left=0.052,bottom=0.110,right=0.984,top=0.923,wspace=0.200,hspace=1.000)

#customize legend
#if we have polygon data e.g ax3v, we have to create dummy ax3v.plot([],[],color='r',alpha=0.5,label='dummy')
ax1.legend() #make sure there is label in ax1.plot()
leg = ax1.legend(loc=9,ncol=2,fontsize=11) #also could use param (prop={'size':11})
leg.get_frame().set_alpha(0.4)

plt.show()
#save the plot
fig.savefig('SAVE_Plot.png',facecolor=fig.get_facecolor())
plt.close()