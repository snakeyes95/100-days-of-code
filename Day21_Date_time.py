#working with date time in python
from datetime import datetime

dateTimeObj=datetime.now()
print(dateTimeObj)

datetime=datetime.strptime('29 Oct 2020', '%d %b %Y')
obs=datetime.date()
print(obs)
print(type(obs))

