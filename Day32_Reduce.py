from functools import reduce
def summation(accum,item):
    print((accum,item))
    return accum + item




if __name__ == '__main__':
    print(reduce(summation,[1,2,3,4,5,6,7],0))