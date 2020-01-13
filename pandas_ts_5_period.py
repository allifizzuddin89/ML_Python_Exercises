#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#TIME SERIES ANALYSIS 2
#Study case : KLSE:IHH

#In stock 2 data is important ; timestamp and period
#timestamp is where we know the price according to time
#we see the revenue in periodic time

#timestamp
#period
#periodindex

import pandas as pd 

y2019 = pd.Period('2019')
print('\n',y2019)

#lets look at the property of period
print('\n',dir(y2019))

#try to use other property

print('\n',y2019.start_time)
print('\n',y2019.end_time)

#mothly time period
m2020 = pd.Period('2020-1',freq='M')
print('\n',m2020)
print('\n',m2020.start_time)
print('\n',m2020.end_time)
print('\n',m2020+1) #gonna be second month

#also similar to
m2020 = pd.Period('2020-2', freq='M')
print('\n',m2020)

#Daily time period
d2019 = pd.Period('2019-02-28',freq='D')
print('\n',d2019)
print('\n',d2019+1) #automatically jump to 1st march, instead of 29th


#what if it is a leap year?
d2020=pd.Period('2016-02-28',freq='D')
print('\n',d2020)
print('\n',d2020+1) #29thFeb

#hourly
h2019 = pd.Period('2019-02-28 14:22:00', freq='H') #it will stay 14:00:00 regardless
print('\n',h2019)
print('\n',h2019.start_time)
print('\n',h2019.end_time)
print('\n',h2019+1)
#also similar with +pd.offset(1) to add 1 hour
print('\n',h2019+pd.offsets.Hour(1))

#Quarterly period
q2019 = pd.Period('2019Q1') #2019 Q1
print('\n',q2019)

#what if fiscal year is not common?
#fiscal year not end Dec
#let say fiscal year end is Jan
q2019 = pd.Period('2019Q1',freq='Q-JAN')
print('\n',q2019.start_time) #fiscal year starts 01/02/2018
print('\n',q2019.end_time) #fiscal year Q1 ends at 30/04/2018

#lets convert the quarterly to monthly
#asfreq
#how to do it?
#can use start or end time
m2019 = q2019.asfreq('M',how="start")
print('\n',m2019)

m2019 = q2019.asfreq('M', how="end")
print('\n',m2019)
#we can see the start month is Feb and end month is April

q2_2019 = pd.Period('2019Q2',freq='Q-JAN')
print('\n',q2_2019.start_time)
print('\n',q2_2019.end_time)

#find quarter difference
print(q2_2019-q2019)

#PERIOD INDEX
idx = pd.period_range('2010','2019',freq='Q-JAN')
print('\n',idx)

#as we noticed, in 2010, the timestamp starts at Q4
print('\n',idx[0].start_time)
print('\n',idx[0].end_time)

#besides giving start and end year
#we can put the number of period

idx = pd.period_range('2010',periods=10,freq='Q-JAN')
print('\n',idx)
print('\n',idx[0].start_time)
print('\n',idx[0].end_time)

print('\n',"2011 Q1 is :")
print('\n',idx[1].start_time)
print('\n',idx[1].end_time)

#create random number generator
import numpy as np 

ps = pd.Series(np.random.randn(len(idx)),idx)
print('\n',ps.index)

#print out only partial index
print('\n',ps['2011':'2015'])

#convert into date time index from period index
pst = ps.to_timestamp()
print('\n',pst)

#pst status, time? period?
print('\n',pst.index)

#convert time index to period index
pst.to_period()
print('\n',pst)

#EXERCISE
#Download THH Financial Report
#Sort data
#Revenue, Expenses and Profit
#add start and end date

#read csv
df = pd.read_csv("klse.ihh.financials.csv")
print('\n',df)

#set index
df.set_index('(MYR)', inplace=True)
print('\n',df)

#trasnpose
df = df.T
print('\n', df)

#convert into period index
print('\n',df.index) #if notice the index is type object, we have to convert it into period index
df.index = pd.PeriodIndex(df.index, freq='Q-JAN') #lets assume the fiscal year starts from January
print('\n',df.index)

#add start date and end date
#use df.index
#issue, we want to add all quarter but they are period object
#use map
#map use function as arguement
#alternative use lambda x

df['start date'] = df.index.map(lambda x: x.start_time)
print('\n',df)

df['end date'] = df.index.map(lambda x: x.end_time)
print('\n',df)