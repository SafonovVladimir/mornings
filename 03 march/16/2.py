def two_sum(nums: list, target: int) -> list:
    stack = set(nums[:1])

    for i in range(1, len(nums)):
        num = target - nums[i]
        if num in stack:
            return [nums.index(num), i]
        stack.add(nums[i])


print(two_sum(nums=[2, 7, 11, 15], target=9))# == [0, 1] # 2 + 7 = 9
print(two_sum(nums=[3, 2, 4], target=6))  # == [1, 2] # 2 + 4 = 6
print(two_sum(nums=[2, 2], target=4))  # == [1, 2] # 2 + 4 = 6
