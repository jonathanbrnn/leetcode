class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        #limit search range to max square root
        right = int(c**0.5)
        while left <= right:
            if left**2 + right**2 == c:
                return True
            elif left**2 + right**2 > c:
                right-=1
            else:
                left+=1
        return False


sol = Solution()
print(sol.judgeSquareSum(1))
