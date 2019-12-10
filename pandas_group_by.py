#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

#1. find max temperature in each city
#2. Find average wind speed per city

import pandas as pd 
import numpy as np 

df = pd.read_csv('weather_by_cities.csv')
print(df)

#Group by cities
#split, apply, combine
#refer realpython groupby for further details

g = df.groupby('city')
print(g)

for city, bandar in g:
    print('\n',city)
    print('\n', bandar)

#access specific dataframe

mumbai_sel = g.get_group('mumbai')
print(mumbai_sel)

#get max temperature and windspeed by city

print(g.max()) #refer above for what is g

#get mean value for temp and windspeed
print(g.mean())

#get all min, max, mean, statistical data
print(g.describe())

#plotting
#%matplotlib inline
g.plot()