class Solution:
    def sortVowels(self, s: str) -> str:

        vowels = "aeiouAEIOU"
        vowels_sorted = []
        t = ""

        for i in range(len(s)):
            if s[i] in vowels:
                vowels_sorted.append(s[i])

        vowels_sorted = sorted(vowels_sorted, key=lambda x: ord(x))

        for i in range(len(s)):
            if s[i] in vowels:
                t += vowels_sorted.pop(0)
            else:
                t += s[i]

        return t



print(Solution().sortVowels("lEetcOde") == "lEOtcede")
