class Solution:
    def countAsterisks(self, s: str) -> int:
        opened = False
        res = 0
        for char in s:
            if char == "|":
                opened = not opened
            elif char == "*" and not opened:
                res += 1
        return res
