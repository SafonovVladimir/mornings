def remove_element(nums: list, value: int) -> int:
    nums[:] = (i for i in nums if i != value)
    return len(nums)

    # return sum(nums.remove(i) for i in range(len(nums)) if nums[i] != val)


print(remove_element([3, 2, 2, 3], 3))  # повертає 2 - твоя функція повинна повертати k = 2,
# c двома елементами nums рівними 2.
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))  # повертає 5 - твоя функція повинна повертати k = 5,
# з п'ятьма елементами nums, що містять 0, 1, 3, 0 та 4.
