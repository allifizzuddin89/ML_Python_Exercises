#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import matplotlib.dates as mdates

#refer https://pythonprogramming.net/converting-date-stamps-matplotlib-tutorial/
def bytespdate2num(fmt, encoding='utf-8'): #FMT IS FORMAT OF DATE STAMP
    strconverter = mdates.strpdate2num(fmt)
    print('\nstrconverter is {}'.format(strconverter))
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    print('\nBytes Converter is {}'.format(bytesconverter))
    return bytesconverter

print('lets print graph')

def graph_data(stock):
    #customizing graph using subplot
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0)) #shape 1,1. location of the figure is at 0,0

    #example of link
    # #also could use yfinance
    # #or yahoo finance premium
    # #or quandl

    #make sure the date is unix timestamp
    #for the sake of this revision hehe
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    print(source_code)

    # #filter
    stock_data = []
    split_source = source_code.split('\n')
    
    # #check line by line
    # #values: Date, close, high, low, open, volume
    # #we only take price, exclude values
    # #we identifies price data only has 6 in a line
    # #anything lower or higher than 6 will be excluded
    # #those data separated by ','
    
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    
    #convert unix date to usable matplotlib date
    # %Y = full year
    # %y = partial year
    # %m = number month
    # %d = number day
    # %H = hours
    # %M = minutes
    # %S = seconds
    # 12-06-2014
    # %m-%d-%Y
    #refer to loaded data
    #the format is %Y%m%d
    
    #date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,delimiter=',',unpack=True, converters={0:bytespdate2num('%Y-%m-%d')})
    #date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,delimiter=',',unpack=True)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          converters={0: bytespdate2num('%Y-%m-%d')})

    #use plot_date to plot data contains date
    ax1.plot_date(date, closep, '-', label='Price') #subplot ax1
    print('\nDate\n ',date)
    print('\nDate Type\n ',date.dtype)

    #fill the plot
    #use alpha to change the opaqueness
    #ax1.fill_between(date, closep,300, alpha=0.5) #(xlabel,yalabel,ymark level also can be a filter, opaqueness)
    #closep[0] means the 1st price in the file
    #use 'where' to use logic
    #'where' will fill the range given
    #in this case 'where' will fill the price above price[0] only
    #'facecolor' is used to change fill's color
    ax1.fill_between(date, closep,closep[0],where=(closep>closep[0]), facecolor='g', alpha=0.5) 

    #lets distinguish between loss and gain
    ax1.fill_between(date,closep,closep[0],where=(closep<closep[0]),facecolor='r', alpha=0.5)

    #plot the loss and gain
    #have to use dummy x,y value
    ax1.plot([],[],linewidth=5,label='Loss',color='r',alpha=0.5)
    ax1.plot([],[],linewidth=5,label="Gain",color='g',alpha=0.5)

    #rotate xticks label to 45 degree
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    #set grid
    ax1.grid(True)

    #change color of x axis and y axis
    ax1.xaxis.label.set_color('b')
    ax1.yaxis.label.set_color('r')

    #set yticks marker range
    ax1.set_yticks([0,175,350,525,700])

    #rotate the date
    #so we can see more date in x label
    #45 degress date label
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    #apply changes on all plot by using plt instead iof ax1
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Stock Graph')
    plt.legend()

    #sometimes the border margin is out of line
    plt.subplots_adjust(left=0.11,bottom=0.191,right=0.977,top=0.926,wspace=0.2,hspace=0)
    plt.show()
    plt.close()

graph_data('TSLA')