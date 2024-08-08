class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ""
        for char in s:
            if char.lower() in "aeiou":
                vowels += char
                s = s.replace(char, "_", 1)
        for vowl in reversed(vowels):
            s = s.replace("_", vowl, 1)
        return s
