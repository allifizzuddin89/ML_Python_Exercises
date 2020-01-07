import datetime as dt 
from pandas.tseries.holiday import *
from pandas.tseries.offsets import CustomBusinessDay

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

malaysia_calendar_2019=CustomBusinessDay(calendar=MY2019BusinessCalendar())
print(malaysia_calendar_2019)


if __name__=='__main__':
    print('\n','Malaysia Holiday Calendar 2019')