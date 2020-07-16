import random
import string

chances=3
random_number=random.randrange(0,100)
while(chances):
    choice=int(input('Please enter your guess .'))
    if random_number != choice:
        chances-=1
        print(f'The number is between {random_number + random.randrange(0,5)} and {random_number - random.randrange(0,5)}')
        print(f'Try and guess the number you have {chances} left!!!!!!!!!')
    else:
         print('congrats you win!')
         break    
    if  chances==0:
        print('Sorry you loose')
        break

    


