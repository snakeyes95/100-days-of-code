number_of_terms=int(input('Enter the number of terms you wish to display'))

n1,n2=0,1
count=0

if number_of_terms <= 0:
    print('please enter a positive number')
else:
    if number_of_terms==1:
        print(n1)
    else:
        while(count<number_of_terms):
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1
