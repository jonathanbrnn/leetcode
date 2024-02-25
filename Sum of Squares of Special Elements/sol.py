class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        for i, num in enumerate(nums):
            if n % (i+1) == 0:
                total += num**2
        return total


sol = Solution()
print(sol.sumOfSquares([1,2,3,4]))
