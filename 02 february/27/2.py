def rotate_list(nums: list, steps: int) -> list:
    return nums[-steps:] + nums[:-steps]


print(rotate_list(nums=[1, 2, 3, 4, 5, 6, 7], steps = 3))# == [5, 6, 7, 1, 2, 3, 4]

# print(rotate_list(nums=[-1, -100, 3, 99], steps = 2))# == [3, 99, -1, -100]
# print(rotate_list([1, 2], 1))# == [3, 99, -1, -100]
print(rotate_list([2, 0, 2, 2], 1))# == [3, 99, -1, -100]
