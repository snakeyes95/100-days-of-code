#understanding working with list 
#to do 
#build a basic shopping cart assign random prices to each of the items in the cart
#indexing a list using [] and the index()
#copying a list the proper and wrong way
#inserting and deleting from a list 
#sorting the list
#reversing the list
#clear the list 
#list unpacking 

import random


shopping_cart=['bottles','pencils','pens','books','smartphones','TV']
prices=[random.randint(1,1000)  for _ in range(len(shopping_cart))]#setting random prices for each of the items in my shopping cart.

#indexing a list can be done as 
print(shopping_cart[0:3])
print(shopping_cart.index('pens'))#index of pens 

shopping_cart_new=shopping_cart

shopping_cart_new[0]='gum'

print(shopping_cart)
print(shopping_cart_new)
#changes will be seen in both the lists as shopping_cart_new is basically accesing the same memory location

#if we want to do a proper copy
shopping_cart_new=shopping_cart[:]

shopping_cart_new[0]='headphones'

print(shopping_cart)
print(shopping_cart_new)
#no change with the shopping_cart

shopping_cart_new=shopping_cart.copy()

shopping_cart_new[0]='shampoo'

print(shopping_cart)
print(shopping_cart_new)
#we can use the copy() as well in this case

#inserting elements
shopping_cart.append('ink')
#will append  towards the end of the list.
print(shopping_cart)
shopping_cart.insert(1,'Diary')
print(shopping_cart)
#insert at a specific position.

shopping_cart.extend(['Camera','Tablet'])
print(shopping_cart)

shopping_cart.pop()
shopping_cart.pop(1)
print(shopping_cart)

shopping_cart.remove('Camera')
print(shopping_cart)

print(shopping_cart.count('Tablet'))
shopping_cart.reverse()
print(shopping_cart)
shopping_cart.sort()
print(shopping_cart)
print(sorted(shopping_cart))

a,b,*other =shopping_cart#list unpacking

print(other)

shopping_cart.clear()#empty the list
print(shopping_cart)




shopping_cart={
    'items':shopping_cart,
    'price':prices,
    'code':'1234'
}


print(shopping_cart)


shopping_cart_dict= shopping_cart.copy()
#same way as list

shopping_cart.update({'code':'0821'})

print(shopping_cart)

print(shopping_cart.get('code',1992))

#to remove the item from your dictionary

shopping_cart.pop('code')
print(shopping_cart)


sample_tuple=(1,2,1,2,3,4,2)
print(sample_tuple.count(2))
print(sample_tuple.index(3))


