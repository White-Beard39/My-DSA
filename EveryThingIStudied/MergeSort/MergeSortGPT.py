def merge_and_count(arr, temp_arr, left, mid, right):
    i = left  # Starting index for the left subarray
    j = mid + 1  # Starting index for the right subarray
    k = left  # Starting index to be sorted
    inv_count = 0

    # Conditions are checked to ensure that i doesn't exceed the mid index and j doesn't exceed the right index
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # There are mid - i inversions, as all the remaining elements in the left subarray (arr[i] to arr[mid])
            # are greater than arr[j]
            temp_arr[k] = arr[j]
            inv_count += mid - i + 1
            j += 1
        k += 1

    # Copy the remaining elements of the left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of the right subarray, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into the original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count


def count_inversions(arr):
    n = len(arr)
    temp_arr = [0] * n
    return merge_sort_and_count(arr, temp_arr, 0, n - 1)


# Example usage:
arr = [1, 5, 2, 3, 6, 3, 8, 9, 4, 6]
print("Number of inversions are:", count_inversions(arr))
