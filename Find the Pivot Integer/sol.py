class Solution:
    def pivotInteger(self, n: int) -> int:
        x = 0
        y = 0
        for i in range(1, n+1):
            x += i
            for j in range(i, n+1):
                y += j
            if x == y:
                return i
            else:
                y = 0
        return -1


sol = Solution()
print(sol.pivotInteger(1))
