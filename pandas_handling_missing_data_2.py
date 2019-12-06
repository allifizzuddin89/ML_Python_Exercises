#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

#replace data
#use replace if there is some random unknown value instead of NaN

import pandas as pd 
import numpy as np 
df = pd.read_csv("weather_data2.csv")
print(df) #shows -99999, -88888 means unknown value

#replace -99999, -88888 using numpy
new_df = df.replace([-99999,-88888], np.NaN)
print(new_df)

#if there is 0 at event column but do not want to chage 0 at other column e.g. temperature to NaN
#using dict

new_df =  df.replace({
    'temperature': -99999,
    'windspeed': [-88888, -99999],
    'event': '0'
},np.NaN)
print(new_df)


#using mapping
#if we want to replace specific value over the dataframe

new_df1 = df.replace({
    -99999:np.NaN,
    -88888:np.NaN,
    'no event':'Sunny'
})
print(new_df1)