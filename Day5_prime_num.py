def check_prime_num(num):
    if num > 1:
        for i in range(2,num):
            if (num % i==0):
                return (f'{num} is not a prime number due to {i}')
        else:
            return (f'{num} is a prime number')

    else:
        return (f'{num} is a prime number')


number=13
print(check_prime_num(number))