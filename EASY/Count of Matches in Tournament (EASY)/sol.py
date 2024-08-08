class Solution:
    def numberOfMatches(self, n: int):
        total = 0
        while True:
            if n % 2 == 0 and n != 1:
                total += n // 2
                n = n//2
            elif n!=1:
                total += int((n-1)/2)
                n = int((n-1)/2+1)
            elif n <= 1:
                return total

sol = Solution()
print(sol.numberOfMatches(14))
