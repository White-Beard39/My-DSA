"""
Given a Right Rotated Array and a target element
return true if there exist a pair who's sum
results in the target element else return false
"""

def find_the_pair(arr: list, trgt : int) -> bool :

    start=end=0

    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            start, end = i+1, i
            break
    print(f"the start is {start} and the end is {end}")
    for i in range(len(arr)):
        if start!=end:
            if arr[start]+arr[end] == trgt:
                print(f"found the elements at {start} and {end}")
                return True
            elif arr[start]+arr[end] <= trgt:
                start = (start+1)%len(arr)
            else : end = (end-1)%len(arr)
        else : return False
   
    

l = [11,85,4,6,8,10]
print(find_the_pair(l, 17))