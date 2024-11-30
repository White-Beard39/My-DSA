def triplets(arr: list) -> list:

    res = []
    eol = len(arr) - 1
    for i in range(len(arr) - 1):
        j = i + 1
        f = False
        while j < eol:
            if arr[j] < arr[eol]:
                f = True
                break
            j += 1
        if arr[i] < arr[j] and f:
            res.append([arr[i], arr[j], arr[eol]])
            break
    print(res)
    return res


l = [5, 3, 7, 6, 9, 1]
print(triplets(l))
