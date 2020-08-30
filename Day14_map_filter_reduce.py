from functools import reduce

list1=[1,2,3,4,5,6,7,8,9,10,11]
list2=[100,102,103,104,105,106]
list3=[1.33456243,12.3214534342,13.435546654,15.213243535]


def greater_10(ls):
    return ls > 10

def custom_sum(first,second):
    return first + second

print(greater_10(int(100)))

#we can also use a map(function,*iterables)
print(list(map(greater_10,list1)))
print(list(map(greater_10,list2)))


print(list(map(round,list3,range(1,len(list3)+1))))

print(list(filter(greater_10,list1)))

print(reduce(custom_sum,list1))



list1=[1,2,3,4,5]
list2=[10,20,30,40,50]

list3=list2 + list1[::-1]

print(list3)