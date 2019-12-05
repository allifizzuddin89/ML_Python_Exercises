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

new_df = df.fillna(method="bfill")

