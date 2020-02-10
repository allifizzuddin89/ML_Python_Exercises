#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.parser import parse 
from matplotlib.dates import strpdate2num  
import matplotlib.pyplot as plt
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

#datefunc = lambda x: datetime.strptime(x.decode("utf-8"), '%Y-%m-%d')

print('lets print graph')

def graph_data(stock):
    #customizing graph using subplot
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0)) #shape 1,1. location of the figure is at 0,0

    #example of link
    # #also could use yfinance
    # #or yahoo finance premium
    # #or quandl

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    print(source_code)

    #filter
    stock_data = []
    split_source = source_code.split('\n')
    
    #check line by line
    #values: Date, close, high, low, open, volume
    #we only take price, exclude values
    #we identifies price data only has 6 in a line
    #anything lower or higher than 6 will be excluded
    #those data separated by ','
    
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
    
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,delimiter=',',unpack=True, converters={0:bytespdate2num('%Y-%m-%d')})
    #date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,delimiter=',',unpack=True, converters={0:datefunc})
    date = parse(date)
    ax1.plot(date, closep, '-', label='Price') #subplot ax1
    print('\nDate\n ',date)
    print('\nDate Type\n ',type(date))

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