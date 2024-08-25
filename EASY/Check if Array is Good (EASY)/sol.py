class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if nums.count(len(nums) - 1) != 2:
            return False

        if len(nums) == 1:
            return False

        for i in range(1, len(nums)):
            if i not in nums:
                return False

        return True
