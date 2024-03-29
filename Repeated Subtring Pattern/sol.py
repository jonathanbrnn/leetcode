class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        current = ""
        l = len(s)
        for char in s:
            current += char
            if current * l == s:
                return True
            else:
                l = l//2


s = "abababab"
sol = Solution()
print(sol.repeatedSubstringPattern(s))
