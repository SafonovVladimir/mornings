def minSubsequence(nums: list[int]) -> list[int]:
    max_num = max(nums)
    max_num_list = [max_num]
    nums.remove(max_num)
    while sum(max_num_list) <= sum(nums):
        max_num_list.append(max(nums))
        nums.remove(max(nums))

    return max_num_list


# nums = [4, 3, 10, 9, 8]
nums = [4, 4, 7, 6, 7]
print(minSubsequence(nums))
