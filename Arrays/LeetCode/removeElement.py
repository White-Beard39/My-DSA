def removeele(nums: list, val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    print(nums)
    return  i


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeele(nums, val))
