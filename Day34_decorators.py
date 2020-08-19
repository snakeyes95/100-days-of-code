def my_first_decorator(fn):
    def wrapper_fn(*args,**kwargs):
        print('**********')
        fn(*args,**kwargs)
        print('**********')
    return wrapper_fn

@my_first_decorator
def say_stuff(text,emoji=':>'):
    print(text,emoji)


if __name__ =='__main__':
    say_stuff('Hi')

    say_stuff('Hello world','-__-')
    