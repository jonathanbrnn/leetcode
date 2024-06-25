class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        s = s.split()
        n = len(s)


        if n != len(pattern):
            return False

        for i in range(n):
            if s[i] not in dic and pattern[i] not in pattern[:i]:
                dic[s[i]] = pattern[i]
            else:
                if s[i] not in dic:
                    return False
                elif dic[s[i]] != pattern[i]:
                    return False

        return True
