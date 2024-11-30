"""
Given k, right rotate the array by k times
"""


def rotate_arr(arr: list, l: int, h: int) -> None:

    while l < h:
        arr[l], arr[h] = arr[h], arr[l]
        l += 1
        h -= 1
    print(arr)


def right_rotate(arr: list, n: int, k: int) -> None:

    k = k % n

    rotate_arr(arr, l=n - k, h=n - 1)
    rotate_arr(arr, l=0, h=n - k - 1)
    rotate_arr(arr, 0, n - 1)

    print(arr)


l = [1, 2, 3, 4, 5, 6]
print(right_rotate(l, len(l), k=8))
# install icecream
