def num_factorial(num):
    if num < 1:
        return 'please enter a valid input value'
    elif num == 0:
        return 1
    elif num == 1:
        return num
    else:
        return num * num_factorial(num-1)



print(num_factorial(4))

