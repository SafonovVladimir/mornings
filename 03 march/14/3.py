def search_insert(nums: list, target: int) -> int:
    if target in nums:
        return nums.index(target)

    nums.append(target)
    new_sort_list = sorted(nums)

    return new_sort_list.index(target)



print(search_insert([1, 3, 5, 6], 2))

# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4
