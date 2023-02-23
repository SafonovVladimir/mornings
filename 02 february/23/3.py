def sum_of_pairs(nums: list, sum_value: int) -> list:
    result = set()

    for num in nums:
        remaind = sum_value - num
        if remaind in result:
            return [remaind, num]
        result.add(num)

    return None

print(sum_of_pairs([11, 3, 7, 5], 10)) # повертає [3, 7] тому, що 3 + 7 = 10
# print(sum_of_pairs([4, 3, 2, 3, 4], 6)) # повертає [4, 2] тому що, 4 + 2 - перша пара, що утворює 6
# print(sum_of_pairs([0, 0, -2, 3], 2)) # повертає None
# print(sum_of_pairs([10, 5, 2, 3, 7, 5], 10)) # повертає [3, 7]
# print(sum_of_pairs([1, -2, 3, 0, -6, 1], -6)) # повертає [3, 7]
# print(sum_of_pairs([20, -13, 40], -7)) # повертає [3, 7]
# print(sum_of_pairs([1, 2, 3, 4, 1, 0], 2)) # повертає [3, 7]
# print(sum_of_pairs([5, 9, 13, -3], 10)) # повертає [3, 7]
