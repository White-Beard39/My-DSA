"""
Given an array of non negative integers
sort the array in such a way that the
even numbers fall to left and odd to right"""

def sort_by_parity( arr : list) -> list :
    
    l,h = 0, len(arr)-1

    while(l<h) :
        if arr[l]%2 == 0 :
            l += 1
        else: 
            if arr[h]%2 == 0 :
                arr[l],arr[h] = arr[h],arr[l]
                h -= 1
                l += 1
            else :
                h -= 1
    return arr


l = [3,4,52,5,6,2,3,5,5,99,6,34,66]
print(sort_by_parity(l))