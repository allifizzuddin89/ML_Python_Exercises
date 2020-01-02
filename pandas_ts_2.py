#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#TIME SERIES ANALYSIS 2
#Study case : KLSE:IHH

#missing dates

import pandas as pd 
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('klse.ihh_no_date.csv')
print(df.head)
print('\n',df)

#call panda date range function
rng = pd.date_range(start="2019-05-15", end="2019-12-8", freq='B') #b means business days, exclude weekend
print(rng)

#set dates index in dataframe
df.set_index(rng,inplace=True)

print('\n',df)

#see index date time in the plot
#run this code in the interactive window (vs code)
df.plot()
plt.show

v1 = df['2019-05-15':'2019-08-30'].Close.mean()
print('\n',v1)

#if we want to display prices on weekend too
#using panda asfrequency method
#regenerate df into new frequency

df1 = df.asfreq('D',method='pad') #padding method
print('\n',df1)

#also can use asfreq to display hourly, 'H'

#check index
print('\n',df.index)

#lets say we dont have any end date but we know the period
rng = pd.date_range(start='2019-01-01',periods=60,freq='B') #will generate 60 businees days
print('\n',rng)

#generate random numbers using numpy
#lets say we also want generate 60 samples prior to those 60 business days
ts = pd.Series(np.random.randint(1,10,len(rng)), index=rng)
print('\n',ts)

#or we want to print out only few on them

print('\n',ts.head(8))

#date_range will not handle holidays
#we can use holiday calendar
#but how???