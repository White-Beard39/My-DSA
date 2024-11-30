"""
Given a list of non negative numbers
find how many number are smaller than the 
current number

Contraaints : 0 <= arr[i] <= 100
"""

def smaller_numbers(arr : list) -> None :

    l = [0]*101

    #initilizing the l with the count of elements in arr
    for i in arr:
        l[i] += 1
    
    #prefix sum
    cnt = 0
    for i in range(len(l)) :
        cnt += l[i]
        l[i] = cnt

    #seggerating the arr
    for i in range(len(arr)) :
        print(f"arr[{i}] is {arr[i]} and l[{i}] i {l[i]}")
        arr[i] = l[arr[i]-1]
    
    print(f"the final arr is {arr}")


l = [8,1,2,2,4,6]
smaller_numbers(l)