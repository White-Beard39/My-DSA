def merge(arr, low, mid, high):
    counter = 0
    arr2 = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            arr2.append(arr[i])
            i += 1
        else:
            counter += mid - i + 1
            arr2.append(arr[j])
            j += 1
    if i > mid:
        while j <= high:
            arr2.append(arr[j])
            j += 1
    if j > high:
        while i <= mid:
            arr2.append(arr[i])
            i += 1
    arr[low : high + 1] = arr2

    return counter


def mergesort(arr: list, low, high):
    counter = 0
    if low >= high:
        return 0
    mid = low + (high - low) // 2
    counter += mergesort(arr, low, mid)
    counter += mergesort(arr, mid + 1, high)
    counter += merge(arr, low, mid, high)

    return counter


l = [1, 5, 2, 3, 6, 3, 8, 9, 4, 6]
print(f"the arr is {l}")
cnt = mergesort(l, 0, len(l) - 1)
print(f"the arr is {l} and counter is {cnt}")
