def my_gen():
    try:
        for i in range(100):
            yield i
    except StopIteration:
        print('stopping')

for i in my_gen():
    print(i)

g=my_gen()

print(next(g))
print(next(g))