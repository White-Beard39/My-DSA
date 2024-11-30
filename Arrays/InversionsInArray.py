"""
In an array if i<j and arr[i]>arr[j] then it
is said to be an inversion. Count the number of 
inversions and return it. Note: the inversions 
for a sorted array is 0"""

def mergecount(arr : list, low : int, mid : int, high : int) -> int :

    count = k = 0 
    i, j = low, mid+1
    temp = arr.copy()
    while(i<=mid and j<=high) :
        if arr[i]>arr[j] : 
            count = mid -i +1
            temp[k] = arr[j]
            k+=1 
            j+=1
        else : 
            temp[k] = arr[i]
            k+=1 
            i+=1
    while ( i<= mid) :
        temp[k] = arr[i]
        k+=1 
        i+=1
    while (j<=high) :
        temp[k] = arr[j]
        k+=1 
        j+=1
    for i in range(len(temp)):
        arr[i] = temp[i]

    return count
    



def divide( arr : list, low : int, high : int) -> int :

    if low>=high : return 0
    mid = (low+high)//2
    l= divide( arr, low, mid)
    h= divide( arr, mid+1, high)
    k = mergecount(arr, low, mid, high)

    return l+h+k

l = [2,5,1,8,9]
print(divide(l,0,len(l)))