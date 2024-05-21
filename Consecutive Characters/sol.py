class Solution:
    def maxPower(self, s: str) -> int:

        if len(s) == 1: return 1

        curr = s[0]
        res = 0

        for i in range(1, len(s)):
            if s[i] == curr[-1]:
                curr += s[i]
            else:
                res = max(res, len(curr))
                curr = s[i]

        res = max(res, len(curr))

        return res
