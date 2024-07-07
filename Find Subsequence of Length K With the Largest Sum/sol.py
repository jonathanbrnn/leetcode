class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        copy_nums = nums.copy()
        copy_nums.sort()
        copy_nums = copy_nums[len(nums) - k:]

        res = []

        for i in range(len(nums)):
            if nums[i] in copy_nums:
                copy_nums.pop(copy_nums.index(nums[i]))
                res.append(nums[i])

        return res
