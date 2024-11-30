def solve(arr: list, trgt: int) -> list:

    mini, maxi = 0, len(arr) - 1

    for i in range(len(arr)):
        if arr[mini] + arr[maxi] == trgt:
            return [mini, maxi]
        elif arr[mini] + arr[maxi] < trgt:
            mini += 1
        elif arr[mini] + arr[maxi] > trgt:
            maxi -= 1

    return [-1, -1]


l = [2, 7, 11, 15]
target = 15
print(solve(l, target))
