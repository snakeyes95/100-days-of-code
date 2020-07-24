list1=[1,2,3,4,5,6,7,8,9,10]
list2=[1,2,3,4,5,6,7,8,9,10]
list3=[1,2,3,4,5]


print(all(i in list2 for i in list1))
print(all(i in list3 for i in list1))