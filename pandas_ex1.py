# import urllib.request
# url = "https://github.com/allifizzuddin89/py/blob/master/pandas/1_intro/nyc_weather.csv"
# filename, headers = urllib.request.urlretrieve(url,filename= "/home/allif_izzuddin/Documents/test/nyc_weather.csv")
# print("download complete...")

import pandas as pd 
df = pd.read_csv("nyc_weather.csv")
print(df)

#also can use data from dict
weather_data = {
    'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017', '1/6/2017'],
    'temperature' : [32, 35, 28, 24, 32, 31],
    'windspread' : [6, 7, 2, 7, 4, 2], 
    'event' : ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}
df = pd.DataFrame(weather_data) #tuples above as Data Frame
print(df)
print(df.shape) #print rows, column
rows, column = df.shape
print(rows)
print(column)
print('#'*100)

#indexing and slicing
print('\n','INDEXING AND SLICING','\n')
print(df.head(2)) #print only few initial rows
print(df.tail(1)) #print last rows

print(df[2:5]) #print row 2 to 4
print(df[:]) #print all, also similar to print(df)
print(df.columns) #print 1st column
print(df.event) #print event column only, similar to df['event']
print(df.day)
print(type(df.event)) #check event object type
print(df[['event', 'day']]) #print event and day column only

print(df['temperature'].max()) #find max temperature
print(df['temperature'].mean()) #means average of temperature
print(df['temperature'].std()) #standard deviation of temperature
print(df.describe()) #print stats on data, quick way

print(df[df.temperature >= 30]) # print temperature 30 degrees and above
print(df[df.temperature == df.temperature.max()]) #print max temperature with all other data
#also similar as:
print(df[df.temperature == df['temperature'].max()]) #if string data type has spaces, prefer this way

print(df['day'][df.temperature == df.temperature.max()]) #print the day with max temperature
print(df[['day','temperature']][df.temperature == df.temperature.max()]) #print the day with max temperature
print('#'*100)


#INDEX

print('\n','INDEX','\n')
print(df.set_index('day')) #does not modify the original data
print(df.set_index('day', inplace = True)) #modify the original data
print(df)

df.reset_index(inplace=True) #reset the replace
print(df)

df.set_index('event', inplace=True) #set event as index
print(df)

print(df.loc['Rain']) #print rain only row, by setting event as index