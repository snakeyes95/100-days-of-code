def fibo(number):
    n1=0
    n2=1
    for _ in range(number):
        yield n1
        temp=n1+n2
        n1=n2
        n2=temp


for i in fibo(100):
    print(i)
