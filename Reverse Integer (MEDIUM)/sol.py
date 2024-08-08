class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        if x < 0:
            answer = -1
        else:
            answer = 1
        sol = str(abs(x))
        sol = ''.join(reversed(sol))
        sol = answer * int(sol)
        if -2**31 < sol < 2**31:
            return sol
        else:
            return 0



sol = Solution()
print(sol.reverse(-1563847412))
