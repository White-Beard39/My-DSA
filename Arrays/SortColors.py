def sort_colors(arr: list) -> list:
    """
    Given an array with 3 numbers
    sort the array in ascending order
    """
    curr = low = 0
    high = len(arr) - 1

    # The idea is to keep the 0s in the beginning, 1s in the middle and 2s in the end
    # We made this possible through the use of 3 pointers

    while curr < high:

        if arr[curr] == 0:
            arr[curr], arr[low] = arr[low], arr[curr]
            curr += 1
            low += 1
        elif arr[curr] == 1:
            curr += 1
        elif arr[curr] == 2:
            arr[curr], arr[high] = arr[high], arr[curr]
            high -= 1
    return arr


l = [0, 0, 1, 2, 1, 2, 1, 2, 0, 0, 0, 2, 1, 2, 2, 1, 0]
print(sort_colors(l))
