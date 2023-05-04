def smallestRangeI(nums: list[int], k: int) -> int:
    max_nums = max(nums) - k
    min_nums = min(nums) + k

    result = max_nums - min_nums

    return result if result >= 0 else 0


nums = [1, 3, 6]
# nums = [10, 0]
# nums = [1]
k = 3
# k = 2
# k = 0

print(smallestRangeI(nums, k))
