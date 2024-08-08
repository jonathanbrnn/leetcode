from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count = 0
        start = 0
        res = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1

            res = max(res, i - start + 1)

        return res
