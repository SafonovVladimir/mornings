def majority_element(nums: list) -> int:
    # result = []
    # for elem in nums:
    #     if nums.count(elem) >= len(nums) / 2:
    #         result.append(elem)
    return max([elem for elem in nums if nums.count(elem) >= len(nums) / 2])


nums1 = [3, 2, 3]
print(majority_element(nums1))
#    Output: 3

nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums2))
# Output: 2
