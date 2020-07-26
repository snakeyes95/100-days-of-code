import re

txt= 'My total life savings amount up to ₹ 471,378 crores'
txt2= 'My total life savings amount up to ₹ 1,471,378 crores'
my_regex=re.compile('\d{1,3}(,\d{3})*')
res=my_regex.search(txt)
res2=my_regex.search(txt2)
print(res.group())
print(res2.group())
print(res.span())
print(res2.span())
