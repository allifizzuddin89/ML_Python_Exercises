#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#TIME SERIES ANALYSIS 1
#Study case : KLSE:IHH


import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('klse.ihh.csv')
print(df)

#another method to import stock historical data is via yfinance and pandas_datareader
#in other py file

#datetimeIndex
#Resampling

#check the date data type
print('\n',type(df.Date[0])) #str type

#change to timestamp

df = pd.read_csv('klse.ihh.csv', parse_dates=['Date'])
print('\n',type(df.Date[0]))

#change index to date column

df = pd.read_csv('klse.ihh.csv', parse_dates=['Date'],index_col='Date')
print('\n',df.index) #verify index

#let say if we want to retrieve only May 2019 data

print('\n',df['2019-05'])

#find average price on May 2019, based on close price
print('\n', df['2019-05'].Close)
print('\n','Mean value is ', df['2019-05'].Close.mean())

#retrive specific date range
print('\n',df['2019-05-01':'2019-06-30'])

#RESAMPLING
#change to monthly stock price
#use average

m1 = df.Close.resample('M').mean()
print('\n',m1)

m1.plot()
plt.show() #run in interactive windows to show the graph (VS Code)


#change to weekly stock price
#use average

w1 = df.Close.resample('W').mean()
print('\n',w1)

w1.plot()
plt.show() #run in interactive windows to show the graph (VS Code)

#refer doc for more frequency code