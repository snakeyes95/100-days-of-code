import random

number_of_rolls=int(input('How many times do u want to roll...'))
print('rollinggggg....!')
while(number_of_rolls):
    die_roll=random.randrange(0,6)
    print(die_roll)
    number_of_rolls-=1
