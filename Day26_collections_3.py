from collections import ChainMap
from collections import namedtuple
#ChainMap is used to combine multiple dictionaries into a list containing dictionaries

dict_1={'a':1,'b':2}
dict_2={'c':3,'d':4}

chain_map_1=ChainMap(dict_1,dict_2)

print(chain_map_1.maps)

#we can even update a dictionary

dict_1.update({'a':17})
print(chain_map_1.maps)#we can see that once the key is updated the ChainMap is also updated.

print(chain_map_1['a'])

dict_3={'e':12,'a':12}

chain_map_2=chain_map_1.new_child(dict_3)

print(chain_map_2.maps)

print(chain_map_2['a'])

print(chain_map_2.keys())
print(chain_map_2.values())

House=namedtuple('House','Rooms,area,Bathrooms,Price')
h1=House('3','12345','3','100000')

print(h1.Rooms)
print(h1)
