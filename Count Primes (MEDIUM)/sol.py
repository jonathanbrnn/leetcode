class Solution:
    def countPrimes(self, n: int) -> int:
        sol = 0
        for i in range(2, n):
            flag = False
            for j in range(2, i):
                if i % j == 0:
                    flag = True
                    break
            if not flag:
                sol += 1
        return sol


sol = Solution()
print(sol.countPrimes(499979))
