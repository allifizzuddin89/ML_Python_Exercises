#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#TIME SERIES ANALYSIS 2
#Study case : KLSE:IHH

import pandas as pd 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 

#import holiday modules
#from pandas.tseries.holiday import USFederalHolidayCalendar #USA Federal Holiday Calendar
from pandas.tseries.offsets import CustomBusinessDay
from pandas.tseries.holiday import *

df = pd.read_csv('klse.ihh_no_date.csv')
print(df)

#it seems there is no date
#so lets put the date

rng =pd.date_range(start="2019-05-15", end="2019-12-08", freq="B")
print('\n',rng)

#we must aware that klse is closed during public holiday too
#so we must refer the date to the calendar
#for the sake of learning we use default pandas libray, USA Holiday Calendar
#create custom calendar, Malaysia Holiday

class MY2019BusinessCalendar(AbstractHolidayCalendar):
    rules: [
        Holiday('Tahun Baru',month=1,day=1),
        Holiday('Thaipusam',month=1,day=21),
        Holiday('Hari Wilayah',month=2,day=1),
        Holiday('Chinese New Year Eve',month=2,day=4),
        Holiday('Chinese New Year',month=2,day=5),
        Holiday('Chinese New Year 2nd day',month=2,day=6),
        Holiday('Hari Buruh',month=5,day=1),
        Holiday('Hari Wesak',month=5,day=19,observance=sunday_to_monday),
        Holiday('Nuzul Al-Quran',month=5,day=22),
        Holiday('Hari Raya Aidilfitri 1',month=6,day=4),
        Holiday('Hari Raya Aidilfitri 2',month=6,day=5),
        Holiday('Hari Raya Aidilfitri 3',month=6,day=6),
        Holiday('Hari Raya Qurban',month=8,day=11,observance=sunday_to_monday),
        Holiday('Hari Kebangsaan',month=8,day=31),
        Holiday('Awal Muharam',month=9,day=1,observance=sunday_to_monday),
        Holiday('Hari Keputeraan YDPA',month=9,day=9),
        Holiday('Hari Malaysia',month=9,day=16),
        Holiday('Deepavali',month=10,day=27,observance=sunday_to_monday),
        Holiday('Maulidurrasul',month=11,day=9),
        Holiday('Krismas',month=12,day=25)

    ]

MCal = CustomBusinessDay(calendar=MY2019BusinessCalendar())
print('\n',MCal)

rng = pd.date_range(start="2019-05-15", end="2019-12-08",freq=MCal)
df.set_index(rng,inplace=True)

print('\n',rng)
print('\n',df)

#is you stay in Johor, Kelantan, Terengganu and Kedah
#the working day will be on Sunday to Thursday
#lets change the calendar on the working day

fri = CustomBusinessDay(weekmask='Sun Mon Tue Wed Thu')
rng1 = pd.date_range(start='2019-05-15',end=2019-12-08,freq=fri)

