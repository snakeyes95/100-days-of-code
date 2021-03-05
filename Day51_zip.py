from itertools import zip_longest

first_name=['adam','eve','clark']
last_name=['jones','light','sanders']


combined_name=zip(first_name,last_name)

print(type(combined_name))

print(list(combined_name))

first_name=['adam','eve']
last_name=['jones','light','sanders']

combined_name=zip(first_name,last_name)

for fname,lname in combined_name:
    print(fname,lname)

#iterators can be iterated only once once a StopIteration is raised we will have to create the object again to iterate through them.
print(list(combined_name))

dict1={'key1':'val1','key2':'val2'}
dict2={'key3':'val3','key4':'val4'}

combined_dict=zip(dict1,dict2)
print(list(combined_dict))


first_name=['adam','eve']
last_name=['jones','light','sanders']

combined_name=zip_longest(first_name,last_name)
print(list(combined_name))