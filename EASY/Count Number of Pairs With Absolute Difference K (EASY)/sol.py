class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0

        for i, num in enumerate(nums):
            for other in nums[i:]:
                if abs(num - other) == k:
                    res += 1

        return res
