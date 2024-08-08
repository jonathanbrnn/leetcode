class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        i = 0
        j = 2
        while j < len(s) + 1:
            curr = s[i:j]
            if curr in s and curr in rev:
                return True
                break
            i += 1
            j += 1
        return False


print(Solution().isSubstringPresent("ausoee"))
