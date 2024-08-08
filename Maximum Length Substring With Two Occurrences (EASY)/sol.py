class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = []
        for i, char in enumerate(s):
            current = char
            for other in s[i+1:]:
                if other not in current:
                    current += other
                elif current.count(other) < 2:
                    current += other
                else:
                    res.append(len(current))
                    break
            res.append(len(current))
        return max(res)
