#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

import pandas as pd 

df = pd.read_excel("stocks.xlsx", header=[0,1]) #double layer header, price + company
print(df)

#stack the header

print('\n',df.stack())

#if only want stack 1st level of header

print('\n',df.stack(level=0)) #transpose 1st header

#unstack

df_unstacked = df.unstack()
print('\n',df_unstacked)

#more complex...
#stacking/unstacking multi level column header
#example, 3 level

df1 = pd.read_excel("stocks_3_levels.xlsx")
print(df1)
print(df1.stack(level=0))