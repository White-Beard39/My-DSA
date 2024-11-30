"""
Given 2 arrays of integer, create a target array 
by inserting nums[i] at index[i]"""

def target_array(nums : list, indx : list) -> list :
    
    trgt_arr = []

    for i in range(len(nums)):
        trgt_arr.insert(indx[i],nums[i])

    return trgt_arr

nums = [0,1,2,3,4]
indx = [0,1,2,2,1]
print(target_array(nums, indx))

"""
Time complexity : O(N)
Space complexity : O(1)
"""