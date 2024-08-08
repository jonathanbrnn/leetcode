class Solution:
    def minLength(self, s: str) -> int:
        while True:
            if "AB" in s:
                s = s.replace("AB", "")
            if "CD" in s:
                s = s.replace("CD", "")
            if "AB" not in s and "CD" not in s:
                return len(s)
                break
