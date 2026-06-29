class Solution:
    def twoSum(self, nums, target: int):
        for i, k in enumerate(nums):
            for j, n in enumerate(nums):
                if i >= j:
                    continue
                if k + n == target:
                    return [i, j]
