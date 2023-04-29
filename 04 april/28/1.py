from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j, n = 0, 1, len(nums)

        while j < n and i < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]

        return nums

nums = [4, 2, 5, 7]
ar = Solution()
print(ar.sortArrayByParityII(nums))
