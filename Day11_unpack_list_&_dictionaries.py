#unpacking lists and dictionary 
l1=[1,2,3,4]
l2=[1,2,3,4,4,5,6,7,8,9]
dict1={'name':'Alex',
        'country':'Australia',
          'prof':'Boxer'}
print(dict1)

def unpack_list(*args):
    length=len(args)
    sum=0
    for i in args:
        sum+=i
    return sum/length

def unpack_dict(**kwargs):
    
    if 'name' in kwargs :
        print(f'name is', kwargs['name'])
    if 'country' in kwargs:
        print(f'country is', kwargs['country'])
    if 'prof'  in kwargs:
        print(f'profession is', kwargs['prof'])
        

print(unpack_list(*l1))
print(unpack_dict(**dict1))