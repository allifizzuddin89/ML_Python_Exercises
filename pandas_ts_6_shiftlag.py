#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#TIME SERIES ANALYSIS 6
#Study case : KLSE:IHH

import pandas as pd 
import numpy as np 

#change Date as timestamp index
#make Date as column index
df = pd.read_csv('klse.ihh.csv', parse_dates=['Date'], index_col='Date')
print(df.head)

#shift prices/data
#by one day shift(1)
s1 = df.shift(1)
print('\n',s1.head)

#shift negative value, to the left of graph
s2 = s1.shift(-2)
print('\n',s2) #2 days to the left

#why shift left ot right?
#finance
#calculate percentage change in certain amount of days
#example:

#create Prev Day Volume column
df['Prev Day Volume'] = df['Volume'].shift(1)
print('\n',df.head(5))

#calculate volume difference in 1 day
df['Volume Change 1 day'] = df['Volume']-df['Prev Day Volume']
print('\n',df)

#difference of close price in 1 day
df["Price Change 1 day"] = df['Close']-df['Close'].shift(1)
print('\n',df)

#5% day return
df['5 day % return'] = ((df['Close']-df['Close'].shift(5))/df['Close'].shift(5))*100
print('\n',df.head(20))

#shift dates
#maintain data point
#simplified data to close price only, for simplification

df = df[['Close']] #which column remain
print('\n',df.head(10))
print('\n',df.index) #pls note, freq=none

#we create freq, business days

df.index = pd.date_range(start='2019-05-15', end='2019-12-08',freq='B')
print('\n',df.index)

#shift the date
print('\n',df)
df1 = df.tshift(1)
print('\n',df1)
