def contains_duplicates(nums: list) -> bool:
    print(nums, set(nums))
    for i in nums:
        if nums.count(i) > 1:
            return True
    return False
    # return nums == set(nums)

nums_list = [9, 9, 9, 9, 9]#, duplicates = Fals

print(contains_duplicates(nums_list))