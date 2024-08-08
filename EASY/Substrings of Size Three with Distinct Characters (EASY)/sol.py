#First Solution:
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        j = 2
        res = 0
        while j < len(s):
            if len(set(s[i:j+1])) == 3:
                res += 1
            i += 1
            j += 1
        return res

#Memory Optimized Solution:
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 2):
            if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:
                res += 1
        return res
