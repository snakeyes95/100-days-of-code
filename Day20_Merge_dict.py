#what if we wanted to keep all the values for the common key?
def megedict(dict1,dict2):
    dict3={**dict1,**dict2}
    for (key,value) in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key]=[value,dict1[key]]
    return dict3
dict1={'pt':44,'geo':55,'eng':44}
dict2={'eng':33,'hind':45,'math':72,'xyz':1}
print(megedict(dict1,dict2))