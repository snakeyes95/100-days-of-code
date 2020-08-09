from collections import OrderedDict
from collections import Counter
from collections import deque
#OrderedDict are useful as they are ordered and will maintain the insertion order even if we change the value of a particular key the order is not changed.
  
ordered_dict=OrderedDict()
ordered_dict['Key1']=1
ordered_dict['Key3']=3
ordered_dict['Key2']=2

for key,value in ordered_dict.items():
    print(key,value)

data=[1,12,23,4,21,1,1,2,3,2,3,1,2,34,2,1]
count_dict=Counter(data)
ordered_dict=OrderedDict(count_dict.most_common())
for key,value in ordered_dict.items():
    print(key,value)


#deque is a list which is optimized for inserting and deleting elements.
deq=deque(['i','g','h'])
print(deq)

#to append element to the right 
deq.append('z')
print(deq)

#to append element to the left
deq.appendleft('a')
print(deq)

deq.pop()#delete from right
print(deq)
deq.popleft()#delete from left
print(deq)

print(deq.count('g'))

deq.clear()
print(deq)