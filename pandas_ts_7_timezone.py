#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#TIME SERIES ANALYSIS 7
#Study case : KLSE:IHH

#2 type of DateTime Objects on Python:
#1.Naive no timezone awareness
#2.Time zone aware datetime

#pytz

import pandas as pd 

df = pd.read_csv('klse.ihh.csv', index_col='Date',parse_dates=['Date'])
print(df)
print('\n',df.index) #notice dtype, datetime64[ns] is naive

#supply timezone
#refer https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
df = df.tz_localize(tz='Asia/Kuala_Lumpur')
print('\n',df.index)

#convert time zone
df = df.tz_convert(tz='US/Eastern')
print('\n',df.index)

#LIST of tz timezone
from pytz import all_timezones
print('\n',all_timezones)

#also can convert this way
df.index = df.index.tz_convert(tz='US/Pacific')
print('\n',df.index)

#how to use timezone
rng = pd.date_range(start='1/1/2018',periods=20,freq='B',tz='Asia/Kuala_Lumpur')
print('\n',rng)

#pytz vs dateutil
#dateutil = provided by operating system
rng = pd.date_range(start='1/1/2018',periods=20,freq='B',tz='dateutil/Asia/Kuala_Lumpur')
print('\n',rng)

#time series using rng 
s = pd.Series(range(20),index=rng)
print('\n',s)

b = s.tz_convert(tz='US/Eastern')
print('\n',b.index)

#what happen if b+s ?
#it will arrange into UTC and sum the series number
print('\n',b+s)