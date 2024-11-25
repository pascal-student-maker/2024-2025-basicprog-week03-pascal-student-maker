import datetime
#  t =    datetime.time(1,2,3)
t = datetime.datetime.now()
print(t)
print('hour :',t.hour)
print('minute:',t.minute)
print('second:',t.second)
print('microsecond:',t.microsecond)

MINYEAR <= year <= MAXYEAR
1 <= month <=12
1 <= day <=number of days in the given month and year
0 <= hour <24
0 <= minute < 60
0 <= second <60
0 <= microsecond < 100000