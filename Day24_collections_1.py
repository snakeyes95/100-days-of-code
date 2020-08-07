#Collections module in python
from collections import Counter
from collections import defaultdict
my_list=[1,2,1,2,3,4,5,3,34,2,5,6,7,1,1,2,1,3,2,1,2,1,2,]
cnt=Counter(my_list)
print(cnt)
print(cnt[1])
print(list(cnt.elements()))
print(cnt.most_common())
deductions={2:1,1:1}
cnt.subtract(deductions)
print(cnt)
data=defaultdict(int)
data['key1']=1
data['key2']=2
print(data['key3'])