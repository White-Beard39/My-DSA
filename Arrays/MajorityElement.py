""""
An element is said to be majority element if the frequency of 
the element is greater than half the length of the list
"""


def majority_element(arr: list, n: int) -> int:

    cnt = 0
    maj_ele = -1

    for i in arr:
        if cnt == 0:
            maj_ele = i 
            cnt += 1
        else :
            if maj_ele != i:
                cnt -= 1
            else : cnt += 1

    print(cnt, maj_ele)

    if arr.count(maj_ele) > n//2 : return maj_ele
    else : return -1


l = [1, 99,3,99,8,99,99,44]
print(majority_element(l, len(l)))
