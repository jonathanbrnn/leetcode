class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        allowed = set(allowed)

        for word in words:
            for char in word:
                if char not in allowed:
                    res += 1
                    break

        return len(words) - res
