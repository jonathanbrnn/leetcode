class Solution:
    def validPalindrome(self, s: str):
        if s == s[::-1]:
            return True

        n = len(s)

        if n == 0:
            return True
        elif n == 1:
            return True
        elif n == 2:
            return True

        l, r = 0, n - 1

        while l < r:
            if s[l] != s[r]:
                curr = s[:l] + s[l+1:]
                if curr == curr[::-1]:
                    return True
                curr = s[:r] + s[r+1:]
                if curr == curr[::-1]:
                    return True
                return False
            l += 1
            r -= 1
