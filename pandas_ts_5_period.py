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

y2020 = pd.Period('2020-1',freq='M')
print(y2020)