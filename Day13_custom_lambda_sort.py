
#sorting a dictionary based on custom functions
d1={'key1':1,'key1234':2,'Key123':4}
#consider that we wanted to sort our dictionary based on the length of the key
print(sorted(d1.items(),key=lambda x:len(x[0])))
print(sorted(d1.items(),key=lambda x:len(x[0]),reverse=True))#we are sorting according to the length of the key
print(sorted(d1.items(),key=lambda x: x[1]))#we can use the same logic to sort a dictionary based on its value