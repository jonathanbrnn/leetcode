class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        rev = []

        for char in s:
            if char.lower() in alphabet:
                rev.append(char)

        res = ""

        for char in s:
            if char.lower() in alphabet:
                res += rev.pop()
            else:
                res += char

        return res
