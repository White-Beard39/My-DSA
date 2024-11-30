def ivers(arr1: list, arr2: list) -> list:
    k = []
    i1 = i2 = 0
    for i in range(len(arr1)):
        if arr1[i1] < arr2[i2]:
            k.append(arr1[i1])
            i1 += 1
        else:
            k.append(arr2[i2])
            i2 += 1
    for i in range(len(arr2)):
        if arr2[i2] < arr1[i1]:
            k.append(arr2[i2])
            i2 += 1
        else:
            k.append(arr1[i1])
            i1 += 1
    return k


def inversions(arr: list, low: int, high: int) -> list:

    if low == high:
        return arr
    else:
        mid = (low + high) // 2
        leftinversion = inversions(arr[low : mid + 1], low, mid)
        rightinversion = inversions(arr[mid + 1 : high + 1], mid + 1, high)

        return ivers(leftinversion, rightinversion)


l = [1, 4, 5, 9, 8]
print(inversions(l, 0, len(l) - 1))
