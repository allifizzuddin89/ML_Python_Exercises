#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

#Reshape data using melt

import pandas as pd

df = pd.read_csv("weather_melt.csv")
print(df)

#set x axis as day, as id variable
#reshape

df1 = pd.melt(df, id_vars=["day"])
print(df1)

#let say we only want to see chicago data only

print('\n',df1[df1["variable"]=="chicago"])

#change 'variable' and 'value' to 'city' and 'temperature'

df1 = pd.melt(df, id_vars=["day"], var_name="city", value_name="temperature")
print('\n',df1)