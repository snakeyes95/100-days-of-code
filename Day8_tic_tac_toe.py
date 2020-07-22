import random
choices=['TL','TC','TR','CL','CC','CR','BL','BC','BR']

winning_condition ={
    'TL':None,
    'TC':None,
    'TR':None,
    'CL':None,
    'CC':None,
    'CR':None,
    'BL':None,
    'BC':None,
    'BR':None
}

board = """ 
        TL  |  TC   |TR
        ------------------
        CL  |   CC  |CR
        ------------------
        BL  |   BC  |BR
        
        """

counter=0


def show_board():
    print(board)

def show_choices():
    print(choices)

def user_choice():
    global winning_condition
    show_choices()
    user_choice=input('Please select which position you want to play from the choices!')
    update_board(user_choice,1)
    winning_condition[user_choice]='X'
    show_board()
    return user_choice

def computer_choice():
        global winning_condition
        comp_choice=random.choice(choices)
        print(f'computer chose {comp_choice}')
        update_board(comp_choice,2)
        winning_condition[comp_choice]='0'
        show_board()
        return comp_choice

def update_choices(choice):
    show_choices()
    choices.remove(choice)
    return 'next move'

def update_board(choice,player):
    if player == 1:
        global board
        board=board.replace(choice,'X')
    else:
        board=board.replace(choice,'0')

def check_winning_conditions():
    global counter
    if winning_condition['TL']=='X' and winning_condition['CC']=='X' and winning_condition['BR']=='X' or winning_condition['TR']=='X' and winning_condition['CC']=='X' and winning_condition['BL']=='X' or winning_condition['TL']=='X' and winning_condition['TC']=='X' and winning_condition['TR']=='X' or winning_condition['CL']=='X' and winning_condition['CC']=='X' and winning_condition['CR']=='X' or winning_condition['BL']=='X' and winning_condition['BC']=='X' and winning_condition['BR']=='X':
        print('User wins')
        return False
    elif winning_condition['TL']=='0' and winning_condition['CC']=='0' and winning_condition['BR']=='0' or winning_condition['TR']=='0' and winning_condition['CC']=='0' and winning_condition['BL']=='0' or winning_condition['TL']=='0' and winning_condition['TC']=='0' and winning_condition['TR']=='0' or winning_condition['CL']=='0' and winning_condition['CC']=='0' and winning_condition['CR']=='0' or winning_condition['BL']=='0' and winning_condition['BC']=='0' and winning_condition['BR']=='0':
        print('Computer wins')
        return False
    elif counter ==9:
        print('Draw')
        return False
    else:
        return True

def play_round():
    global counter
    while(check_winning_conditions()):
        choices=user_choice()
        print(choices)
        update_choices(choices)
        counter+=1
        show_board()
        update_choices(computer_choice())
        show_board()
        print(winning_condition)    
        counter+=1
        print(counter)

if __name__ == '__main__':
    show_board()
    play_round()