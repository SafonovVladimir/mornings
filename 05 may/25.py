def findTheDistanceValue(arr1: list[int], arr2: list[int], d: int) -> int:
    count = 0
    for num1 in arr1:
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                count += 1
                break
    return len(arr1) - count


arr1 = [-3, 10, 2, 8, 0, 10]
arr2 = [-9, -1, -4, -9, -8]
d = 9

print(findTheDistanceValue(arr1, arr2, d))
