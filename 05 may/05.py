def sortArrayByParity(nums: list[int]) -> list[int]:
    # result_list = []
    #
    # for num in nums:
    #     if num % 2 == 0:
    #         result_list.insert(0, num)
    #     else:
    #         result_list.append(num)
    #
    # return result_list
    return sorted(nums, key=lambda x: x % 2)

nums = [3, 1, 2, 4]
print(sortArrayByParity(nums))
