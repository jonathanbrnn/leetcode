from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for bit in range(32):
            count = 0
            for num in nums:
                if num & (1 << bit):
                    count += 1
            if count > 0:
                res += (1 << bit) * (1 << (n - 1))

        return res
