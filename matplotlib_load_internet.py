#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

import numpy as np  
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

print('lets print graph')

def graph_data(stock):   
    #example of link
    # #also could use yfinance
    # #or yahoo finance premium
    # #or quandl

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    print(source_code)

    #source_code = requests.get(stock_price_url)
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
    
    plt.plot(date, closep, '-', label='Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Stock Graph')
    plt.legend()
    plt.show()

graph_data('TSLA')