#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#TIME SERIES ANALYSIS 2
#Study case : KLSE:IHH

#ununiformity input data
#use to_datetime to convert date into single format

import pandas as pd 

date = ['2020-01-07','Jan 7,2020','01/07/2020','2020.01.07','2020/01/07','20200107']

d1 = pd.to_datetime(date)
print(d1)

#time
#convert into 24hrs
date = ['2020-01-07 2:30:00 PM','Jan 7,2020 14:30:00','01/07/2020','2020.01.07','2020/01/07','20200107']

d2 = pd.to_datetime(date)
print('\n',d2)

#convert date
#USA : mm/dd/yy
#EU : dd/mm/yy

d3 = pd.to_datetime('07/01/2020') #actually we want to say 7th Jan (EU) but by default it is USA format
print('\n',d3)

#change it 

d3 = pd.to_datetime('07/01/2020', dayfirst=True)
print('\n',d3)

#custom format
#try use '#' as separator

d4 = pd.to_datetime('07#01#2020',format='%d#%m#%Y',dayfirst=True)
print('\n',d4)

#let say if there is rubbish input data

date = ['2020-01-07','Jan 7,2020','01/07/2020','2020.01.07','2020/01/07','blablabla']

# d1 = pd.to_datetime(date)
# print(d1) #it will display "Unknown string format"
#fix it with error type

d1 = pd.to_datetime(date,errors='ignore')
print('\n',d1)

#but if want use other data and eliminate the rubbish input data
#use 'coerce'

d1 = pd.to_datetime(date,errors='coerce')
print('\n',d1) #it will display NaT

#EPOCH
#number of seconds that have passed since Jan 1, 1970 00:00:00 UTC
#declare as s(seconds)

t = 1578423333 #epoch time 7th Jan 2020, 06:55:33 PM
d1 = pd.to_datetime(t,unit='s')
print('\n',d1)

t = 1578423333 #epoch time 7th Jan 2020, 06:55:33 PM
d1 = pd.to_datetime([t],unit='s') #can put t as an array function
print('\n',d1)

#convert into int64
#convert back into epoch
d2 = d1.view('int64')
print('\n',d2)