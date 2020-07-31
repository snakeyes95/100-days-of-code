def bin_search_rec(ls,element,start_idx,end_idx):
    print(f'Current list is {ls[start_idx:end_idx+1]}')
    if ls[start_idx:end_idx+1]:
        if start_idx > end_idx:
            print(start_idx,end_idx)
            return 'done'
        
        mid_idx = (start_idx + end_idx)//2

        if ls[mid_idx] == element:
            return f'element found at idx {mid_idx}'

        if element < ls[mid_idx]:
            return bin_search_rec(ls,element,start_idx,mid_idx - 1)
        else:
            return bin_search_rec(ls,element,mid_idx + 1,end_idx)
    return 'Element not found!'    

print(bin_search_rec([1,2,3,4,5,7,8,9,10],11,0,len([1,2,3,4,5,7,8,9,10])+1))