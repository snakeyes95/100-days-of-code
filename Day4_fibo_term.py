def fibo(n):
    if n <= 0:
        return 'please enter a correct input'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))


print(fibo(7))