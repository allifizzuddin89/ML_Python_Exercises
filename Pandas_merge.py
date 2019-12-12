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
#merge by default acts like subset OR
#change it to subset and
#outer, right, left

us_humid_df = pd.DataFrame({
    "City" : ["Baltimore","New York","Chichago"],
    "Humidity" : [12,32,70]
})
print(us_humid_df)

us_temp_df = pd.DataFrame({
    "City" : ["Baltimore","Oregon","Santana","New York"],
    "Temperature" : [-1,12,23,6]
})
print(us_temp_df)

df2 = pd.merge(us_humid_df,us_temp_df,on="City",how="outer")
print(df2) #it seems this does not need index at df definition

df2 = pd.merge(us_humid_df,us_temp_df,on="City",how="left")
print(df2)

df2 = pd.merge(us_humid_df,us_temp_df,on="City",how="right")
print(df2)

#if need to know the df comes from which part

df2 = pd.merge(us_humid_df,us_temp_df,on="City",how="outer", indicator=True)
print(df2)

#SUFFIXES
#when both df has same column

us_west_df1 = pd.DataFrame({
    "City" : ["Baltimore","Oregon","Santana","New York"],
    "Temperature" : [-1,12,23,6],
    "Humidity" : [4,7,9,8]
})
print(us_west_df1)

us_west_df = pd.DataFrame({
    "City" : ["Baltimore","Oregon","Santana","New York"],
    "Temperature" : [-1,13,2,16]
})
print(us_west_df)

df4 = pd.merge(us_west_df,us_west_df1,on="City")
print(df4) #it shows column with appended x and y

#change x and y to left and right
#use suffixes

df4 = pd.merge(us_west_df,us_west_df1,on="City", suffixes=("_left","_right"))
print(df4)
