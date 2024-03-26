class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n = len(nums)
        for i in range(1, n + 1):
            if i not in nums_set:
                return i
        return n + 1
