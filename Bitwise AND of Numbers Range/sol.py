class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        total = 0
        while left < right:
            total += 1
            left >>= 1
            right >>= 1
        return left << total

sol = Solution()
print(sol.rangeBitwiseAnd(5,7))
