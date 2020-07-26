import re
txt='Hello world !!! today is a great day.'

res=re.findall('[aeiouAEIOU]',txt)

print(res)

res2=re.sub('[aeiouAEIOU]','$',txt)
print(res2)