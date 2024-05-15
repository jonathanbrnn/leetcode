class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        if n == 0:
            return 0
        for i in range(2, n):
            f.append(f[i-1] + f[i-2])
        return f[-1] + f[-2]


print(Solution().fib(4))
