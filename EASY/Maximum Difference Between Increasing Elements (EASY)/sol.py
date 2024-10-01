class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1

        for i in range(len(nums) - 1):
            curr_max = max(nums[i:])
            if curr_max > nums[i]:
                res = max(res, abs(curr_max) - nums[i])

        return res
