#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

import pandas as pd 

#USE CSV AS DATAFRAME

df = pd.read_csv('nyc_weather.csv')
print(df)


#USE EXCEL AS DATAFRAME

df = pd.read_excel("nyc_weather.xlsx", "nyc_weather") #pd.read_excel("file", "sheetname")
print(df)


#USE PYTHON DICT

weather_data = {
    'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017', '1/6/2017'],
    'temperature' : [32, 35, 28, 24, 32, 31],
    'windspread' : [6, 7, 2, 7, 4, 2], 
    'event' : ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}

df = pd.DataFrame(weather_data)
print(df)


#USE TUPLES

weather_data = [
    ('1/1/2017', 32, 6, 'Rain'),
    ('1/2/2017', 35.7, 'Sunny'),
    ('1/3/2017', 28, 'Snow')
    ]

#we have to add data name column to the dataframe
df = pd.DataFrame(weather_data, columns= ["daya", "temperature", "wuindspeed", "event"])
print(df)


#USE LIST

weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 40, 'windspeed': 4, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 18, 'windspeed': 9, 'event': 'Snow'},
    {'day': '1/4/2017', 'temperature': 19, 'windspeed': 4, 'event': 'Snow'},
]
df = pd.DataFrame(weather_data)
print(df)