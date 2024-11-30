"""
Given non negative numbers in a list, there will 
only be one number that occurs odd number of times
"""

def single_number(arr : list) -> int :

    ans = 0

    for i in arr :
        ans = ans ^ i

    return ans

l = [1,2,4,5,4,1,2,5]
print(single_number(l))