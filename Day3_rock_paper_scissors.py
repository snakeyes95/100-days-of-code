import random

choices=['rock','paper','scissors']
user_points=0
computer_points=0




while(True):
    computers_choice=random.choice(choices)
    while(True):
        user_choice=input(f'please enter your choice from {choices}')

        if user_choice not in choices:
            print('please enter the correct option')

        else:
            break


    if computers_choice == user_choice:
        print('Match draw!')
    if computers_choice == 'rock' and user_choice == 'scissors':
        print('Computer wins')
        computer_points+=1
    elif computers_choice == 'paper' and user_choice == 'rock':
        print('Computer wins')
        computer_points+=1
    elif computers_choice == 'scissors' and user_choice == 'paper':
        print('Computer wins')
        computer_points+=1
    else:
        print('user wins!')
        user_points+=1
    print(f'Current score Computer {computer_points} user {user_points}')
    if user_points==3 or computer_points==3:
        print(f'Current winner Computer {computer_points} user {user_points}')
        break
print('Good game!')