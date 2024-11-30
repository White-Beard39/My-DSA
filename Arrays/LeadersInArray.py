"""
arr[i] is said to be a leader if there is no element 
greater towards it's right. 
Note: The right most element is always a leader
"""

from Utils.utils import log_records

def leader(arr : list) -> list :

    maxi = arr[-1]
    leds = [maxi]
    for i in range (len(arr)-2, -1, -1):
        if arr[i]> maxi:
            maxi = arr[i]
            leds.append(maxi)       
    return leds


l = [8,4,2,3,1,5,4,2]
# print(leader(l))
print(log_records(leader)(l))