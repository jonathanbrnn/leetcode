class Solution:
    def maxScore(self, s: str) -> int:
        i = 1
        res = 0
        while i < len(s):
            res = max(s[:i].count("0") + s[i:].count("1"), res)
            print(s[:i], s[i+1:])
            i += 1
        return res
