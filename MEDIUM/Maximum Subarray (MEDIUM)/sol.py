class Solution:
    def maxSubArray(self, nums: list) -> int:
        best = min(nums) - 1
        current = 0
        for num in nums:
            current = max(num, current+num)
            best = max(best, current)
        return best



nums = [5,4,-1,7,8]
sol = Solution()
print(sol.maxSubArray(nums))
