import time 
from datetime import date


year,month,day=input('please enter your birthday in yyyy mm dd format').split()

birth_day=date(int(year),int(month),int(day))
print(birth_day)
today=date.today()
print(today)
if birth_day < today:
    birth_day=birth_day.replace(year=today.year+1)
    days_left=abs(birth_day - today)
else:
    days_left=abs(birth_day - today)

print(f'The number of days left for your birthday is {days_left.days}')