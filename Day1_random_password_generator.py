#design a simple random password generator which will generate a random 8 digit password with symbol Uppercase lower case  etc.
#we want atleast 1 upper case letter the remaining 7 can be symbols and lowercase letters as follows.
import random 
import string
uppercase_letter=list(random.choice(string.ascii_uppercase))
punctuations=random.choices(string.punctuation,k=2)
remaining=random.choices(string.ascii_lowercase+string.digits,k=5)
final_list=uppercase_letter+punctuations+remaining
random.shuffle(final_list)

random_gen_password=''.join(final_list)

print(f'random generated password is given as {random_gen_password} use it wisely!!!')