def search_in_rotated_sorted_array(arr: list, trgt: int) -> int:

    l = len(arr)
    pivot = None
    for i in range(1, l):
        if arr[i - 1] > arr[i]:
            pivot = i
    print(f"the pivot is {pivot}")
    print(f"the arr is {arr}")
    if pivot:
        left = pivot - 1
        right = pivot
        while left != right:
            if arr[left] + arr[right] == trgt:
                return True
            elif arr[left] + arr[right] < trgt:
                right = (right + 1) % l
            else:
                left = (l + left - 1) % l
        print("Didn't find any pair")
        return False
    else:
        return False


l = [7, 8, 1, 2, 3, 4]
trgt = 0
print(search_in_rotated_sorted_array(l, trgt))
