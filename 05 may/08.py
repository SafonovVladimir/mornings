def isMonotonic(nums: list[int]) -> bool:
    # if (nums[0] <= nums[-1] and nums == sorted(nums)) or (
    #         nums[0] >= nums[-1] and nums == sorted(nums, reverse=True)):
    #     return True
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)


# nums = [1, 2, 2, 3]
# nums = [1, 3, 2]
nums = [1, 1, 1]

print(isMonotonic(nums))
