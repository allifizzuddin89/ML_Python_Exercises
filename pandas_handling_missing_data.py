#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

#HANDLING MISSING DATA
#fillna
#dropna
#interpolate

import pandas as pd 
df = pd.read_csv("weather_data.csv")
print(df)
print(type(df.day[0])) #str type, we want to force convert it into date type
df = pd.read_csv("weather_data.csv", parse_dates=["day"]) #parse day column as date
print(type(df.day[0])) #convert it into timestamp already
df.set_index('day', inplace=True) #set day as index
print(df)

#fillna
#replace NaN with other

new_df = df.fillna(0) #convert NaN to 0 in dataframe
print(new_df)

#if wants to replace NaN to specified object, use dict as below
new_df = df.fillna({
    'temperature' : 0,
    'windspeed' : 0,
    'event' : 'no event'
})
print(new_df)

#look at temperature column, some 0 data is not appealing
#how interpolate it?
#use fillna + ffill(forward fill) / bfill(backward method)

new_df = df.fillna(method="ffill") #forward fill method, copy prev value
print(new_df)

new_df = df.fillna(method="bfill") #backward fill method, copy next value
print(new_df)

new_df = df.fillna(method="bfill", axis="columns") #use axis to copy data horizontally
print(new_df)

new_df = df.fillna(method="ffill", limit=2) #add limit, copy prev value only as per set limit
print(new_df)

#Interpolate using interpolate()
#linear interpolate
#refer pandas doc for more interpolate method

new_df = df.interpolate() #linear interpolate
print(new_df)

new_df = df.interpolate(method="time") #time method, estimate missing values
print(new_df)

#Drop rows which has incomplete data

new_df = df.dropna() #drop all row which has incomplete data
print(new_df)

new_df = df.dropna(how="all") #drop row which has all NaN
print(new_df)

new_df = df.dropna(thresh=1) #keep the row which as 1 non NaN
print(new_df)

#How to insert missing date
#using date_range
#DatetimeIndex
#reindex

dt = pd.date_range('01-01-2017','01-11-2017')
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)
print(df)