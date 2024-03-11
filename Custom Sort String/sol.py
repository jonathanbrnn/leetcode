class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sol = ""
        for char in order:
            sol += char * s.count(char)
            s = s.replace(char, "")
        sol += s
        return sol
