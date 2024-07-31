class Solution:
    def finalString(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            if s[i] == "i":
                res = res[::-1]
            else:
                res += s[i]

        return res
