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

df_stacked = df.stack()
print('\n',"UNSTACK")
print('\n',df_stacked.unstack()) 

#more complex...
#stacking/unstacking multi level column header
#example, 3 level

print('\n','Unstacking multi level column header')
df1 = pd.read_excel("stocks_3_levels.xlsx", header=[0,1,2])
print('\n',df1)
# df2 = df1
print(df1.stack(level=0))
df1.to_excel("stocks_3_level_edit.xlsx", sheet_name="Stock1")
# df2.to_excel("stocks_3_level_edit.xlsx", sheet_name="Stock2")
