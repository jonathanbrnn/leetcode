class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maximum = max(nums)
        minimum = min(nums)
        for i in range(len(nums)):
            if minimum < nums[i] < maximum:
                return nums[i]
        return -1
