"""
Given an array formed with 3 numbers
You need to arrange it in a way that 
all the three numbers are grouped"""
import math
from Utils.utils import log_records
def dutch_nf(arr : list ) -> list :

    curr = low = 0
    high = len(arr)-1

    for i in range(len(arr)):
        print(f"the arr is {arr} {low} {curr} {high}")

        if arr[i] == 0 :
            arr[curr],arr[low] = arr[low], arr[curr]
            curr +=1
            low += 1
        elif arr[i] == 1 :
            curr += 1
        elif arr[i] == 3 and curr < high:
            arr[curr], arr[high] = arr[high], arr[curr]
            high -= 1
            curr += 1
        
    return arr


l = [3,1,0,1,3,1,1,1,3,1,0,3,3,3,3,3,1,1,1,1,0]
print(log_records(dutch_nf)(l))