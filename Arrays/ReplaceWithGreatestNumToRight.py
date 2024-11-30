"""
Replace the element with the greatest 
element in it's right subarray.       
"""

def goat_right(arr : list) -> list :

    maxi = 0

    for i in range(len(arr)-1, -1, -1):
        if i == len(arr)-1 : 
            maxi = arr[i]
            arr[i] = -1
        else : 
            temp = maxi
            maxi = max(maxi, arr[i])
            arr[i] = temp
    return arr

l = [17,18,5,4,6,1]
print(goat_right(l))