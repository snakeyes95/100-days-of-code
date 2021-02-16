def outer_func():
    x=10
    y=20
    print('Outer function!')#here x and y are both acting as free variables 
    def nested_func(num):#the nested function still has access to the variables x and y even if outer_func is out of memory
        res=x+y+num
        print(res)
    return nested_func


if __name__ == '__main__':
    temp_var=outer_func()

    temp_var(30)#the nested function can still be called after outer function has completed execution
    temp_var(40)#the data is bound to the code and not to memory
