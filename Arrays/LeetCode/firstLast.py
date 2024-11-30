def fl(nums: list, target: int) -> list:

    # res = []
    # cnt = 0
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         if cnt == 2:
    #             break
    #         res.append(i)
    #         cnt += 1
    # print(res, cnt)
    # return [-1, -1] if cnt != 2 else res

    mid = len(nums) // 2
    if nums[mid] == target:
        return mid
    else:
        k = f1(nums[:mid], target)
        return k


nums = []
target = 0
print(fl(nums, target))
