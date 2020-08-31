
def check_anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    else:
        for i in range(len(str1)):
            if str1[i] in str2:
                str2=str2.replace(str1[i],'')
                if len(str2)==0:
                    print('chk')
                    return True
            else:
                return False

if __name__ == '__main__':
    str1='army'
    str2='mary'
    print(check_anagram(str1,str2))