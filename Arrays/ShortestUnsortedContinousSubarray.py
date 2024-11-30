"""
Given an array return the length of the 
array upon whose sorting will return a
sorted array
"""

def shortest_unsorted(arr : list) -> int :
    """TC = O(n)2 and SC = O(1)"""

    start, stop = len(arr), 0
    for i in range(len(arr)):
        for j in range (i+1, len(arr)) :
            if arr[i]>arr[j] :
                start = min(start, i)
                stop = max(j,stop)
            
    print(start, stop)

    return stop-start+1 if stop - 1 >=0 else 0

def shortest_unsorted_nlogn(arr: list) -> int :

    start, stop = len(arr), 0

    temp_arr = arr.copy()
    temp_arr.sort()

    print("the sorted temp arr is ", temp_arr)
    print("the normal array is ", arr)
    for i in range(len(arr)):
        if arr[i] != temp_arr[i]:
            start = min(start,i)
            stop  = max(stop, i)
        
    print(f'start and stop are {start} {stop}')

    return stop-start+1 if stop-1 >= 0 else 0 

def shortest_unsorted_n(arr : list) -> int :

    stk = [0]
    start, stop = len(arr), 0

    for i in range(1,len(arr)) :
        if arr[stk[-1]] <= arr[i] :
            stk.append(i)
        else :
            start = min(start, stk.pop())

    stk.clear()
    stk.append(len(arr)-1)
    for i in range(len(arr)-2,-1,-1):
        if arr[stk[-1]] >= arr[i]:
            stk.append(i)
        else :
            stop = max(stop,stk.pop())

    return stop-start+1 if stop != 0 else 0
l = [1,2,5,5]
# print(shortest_unsorted(l))
# print(shortest_unsorted_nlogn(l))
print(shortest_unsorted_n(l))