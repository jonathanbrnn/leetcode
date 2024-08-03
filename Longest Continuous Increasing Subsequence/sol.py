class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1

        res = max(res, curr)

        return res
