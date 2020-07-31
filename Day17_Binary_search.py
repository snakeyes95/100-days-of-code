def bin_search_itr(ls,element):
    start_idx=0
    end_idx=len(ls)
    mid_idx=0


    while(start_idx <= end_idx):
        print(f'Current list is {ls[start_idx:end_idx+1]}')
        if ls[start_idx:end_idx+1]:
            mid_idx=(start_idx+end_idx)//2
            if ls[mid_idx] == element:
                return f'element found at idx {mid_idx}'
            
            elif element < ls[mid_idx]:
                end_idx=mid_idx - 1

            else:
                start_idx=mid_idx + 1
        else:
            return 'Element not found'

    
        
print(bin_search_itr([1,2,3,4,5,7,8,9,10],19))