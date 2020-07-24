sample=[7,0,1,2,3,4,1,5,6,7,8]
duplicate=[]
indexes=[]

for index,value in enumerate(sample):
    if sample.count(value)>1:
        if value not in duplicate:
            duplicate.append(value)
            indexes.append(index)
    else:
        continue
print(duplicate)
print(indexes)