class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        current = ""
        l = len(s)
        for char in s:
            current += char
            m = l // len(current)
            if current * m == s and m != 1:
                return True
        return False


s = "abcabcabcabc"
sol = Solution()
print(sol.repeatedSubstringPattern(s))
