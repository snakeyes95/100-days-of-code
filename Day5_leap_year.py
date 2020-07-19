def check_leap(year):
    return (((year % 4 == 0)and (year%100 !=0))or(year%400 == 0))



year = 2025

if (check_leap(year)):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')