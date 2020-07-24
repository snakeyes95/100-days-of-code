original_list=[1,2,3,4,5,1,2,3,5,6,7,8,11,22,33,44,55,66,66]
duplicate_list=[]

def find_duplicates(ls):
    for i in ls:
        if ls.count(i) > 1:
            if i not in duplicate_list:
                duplicate_list.append(i)
    return duplicate_list





if __name__ == '__main__':
    print(find_duplicates(original_list))


