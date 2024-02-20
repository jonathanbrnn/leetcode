class Solution:
    def maxXOR(self, nums) -> int:
        values = []
        for i, num in enumerate(nums):
            for other in nums[:i]:
                values.append(num ^ other)
        return max(values)


nums = [14,70,53,83,49,91,36,80,92,51,66,70]
sol = Solution()
print(sol.maxXOR(nums))
