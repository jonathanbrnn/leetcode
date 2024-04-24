class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        i = 0
        j = 3
        while n > 2:
            t.append(sum(t[i:j]))
            print(t[i:j])
            i += 1
            j += 1
            n -= 1
        return t[-1]


print(Solution().tribonacci(25))
