def moving_zeros(nums: list) -> list:
    for item in nums:
        if item == 0:
            nums.remove(item)
            nums.append(item)
    return nums

print(moving_zeros([1, 0, 1, 2, 0, 1, 3])) # повертає [1, 1, 2, 1, 3, 0, 0]
print(moving_zeros([0, 2, 0, 1, 1, 0, 3])) # повертає [2, 1, 1, 3, 0, 0, 0]
print(moving_zeros([0,0])) # повертає [0, 0]
print(moving_zeros([])) # повертає []
