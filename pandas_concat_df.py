#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

import pandas as pd 
india_weather = pd.DataFrame({
    "City" : ["Mumbai","Delhi","Bangalore"],
    "Temperature" : [32,45,30],
    "Humidity" : [80,60,78]
})
print(india_weather)

us_weather = pd.DataFrame({
    "City" : ["New York","Chichago","Orlando"],
    "Temperature" : [21,14,35],
    "Humidity" : [68,65,75]
})
print(us_weather)


#CONCAT OR JOIN MULTIPLE DATAFRAME INTO ONE

df = pd.concat([india_weather, us_weather])
print(df) #see index, original index

df = pd.concat([india_weather, us_weather], ignore_index=True) #continuous index
print(df) #see index

#Add additional index based on subset in dataframe
#In this case based on location, which equal to each separate dataframe

df = pd.concat([india_weather, us_weather], keys=["India","US"])
print(df)

print(df.loc["US"])

#Concat 2 different data horizontally
#windspeed + temperature for Mumbai
#set index mumbai=0, delhi=1, bangalore=2
#therefore it will be arranged according to index

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





#Joint df with series of event

s = pd.Series(["Rain","Dry","Humid"],name="Event")
print(s)

df = pd.concat([india_temperature_df,s], axis=1)
print(df)