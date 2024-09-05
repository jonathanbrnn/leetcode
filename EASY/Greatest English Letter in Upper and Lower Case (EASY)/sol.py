class Solution:
    def greatestLetter(self, s: str) -> str:
        cou = set(s)
        curr = 0
        res = ""

        for char in s:
            if char.isupper():
                if char.lower() in cou and ord(char) > curr:
                    curr = ord(char)
                    res = char

        return res
