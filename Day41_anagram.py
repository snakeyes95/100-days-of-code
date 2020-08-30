def check_anagram(str1,str2):
    lst1=[i for i in str1]
    lst2=[i for i in str2]
    if len(lst1) != len(lst2):
        return False
    else:
        lst1.sort()
        lst2.sort()
        if lst1 == lst2:
            return True
        else:
            return False




if __name__ == '__main__':
    str1=input('Enter string one')
    str2=input('Enter string one')
    print(check_anagram(str1,str2))