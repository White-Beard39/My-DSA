class BinarySearch:

    def __init__(self, arr: list, target: int):
        self.arr = arr
        self.target = target

    def bin_search(self) -> int:
        # returns the first found element position
        low, high = 0, len(arr) - 1

        while low <= high:

            mid = low + (high - low) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return f"Not Found"

    def first_or_last_ele_in_bin_sesarch(self) -> int:
        # returns the first index of a found element
        low, high = 0, len(arr) - 1
        res = None
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                res = mid
                # high = mid - 1    # to get the first element
                low = mid + 1  # to get the last element
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return res


arr = [2, 4, 6, 8, 9, 12, 12, 12, 15, 17, 19, 33, 66, 77, 551]
target = int(input("Please enter a number : "))
(
    print("The index of the element is", arr.index(target))
    if target in arr
    else print("Not Found")
)
find_element = BinarySearch(arr, target)
print(find_element.first_ele_in_bin_sesarch())
