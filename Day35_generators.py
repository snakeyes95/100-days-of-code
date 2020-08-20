#generator comprehensions
#a generator comprehension is memory efficient as it is not evaluated immediatley but is used as 
#an iterable and will generate values one by one in the iteration this makes it memory efficient.
g=(i for i in range(100))
sum=0
for num in g:
    sum=sum+num
print(sum)
print(list(g))