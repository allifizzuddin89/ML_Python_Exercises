#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

import pandas as pd 

india_windspeed_df = pd.DataFrame({
    "City" : ["Mumbai", "India", "Bangalore"],
    "Windspeed" : [12,7,3],
},index=[0,1,2])
print(india_windspeed_df)

india_temperature_df = pd.DataFrame({
    "City" : ["Mumbai", "India", 'Bangalore'],
    "Temperature" : [34, 44, 12]
}, index=[0,1,2])
print(india_temperature_df)

df = pd.concat([india_temperature_df, india_windspeed_df])
print(df) # see column

#Fix 

df = pd.concat([india_temperature_df, india_windspeed_df], axis=1)
print(df) #see column

#Fix
#Use merge
#join both temperature and wind speed

df1 = pd.merge(india_windspeed_df,india_temperature_df, on="City") #pick City as ref column
print(df1)

#What happen if merged dataframe has no common element, e.g. city
#it will merge anything is common
#use outer
#merge by default acts like subset or
#change it to subset and

us_humid_df = pd.DataFrame({
    "City" : ["Baltimore","New York","Chichago"],
    "Humidity" : [12,32,70]
})
print(us_humid_df)

us_temp_df = pd.DataFrame({
    "City" : ["Baltimore","Oregon","Santana","New York"]
})