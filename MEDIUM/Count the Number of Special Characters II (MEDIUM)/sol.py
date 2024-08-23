class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        if word == word.lower() or word == word.upper():
            return 0

        dic = {}
        res = 0

        for i, char in enumerate(word):
            if char.islower():
                dic[char] = i
            elif char not in dic:
                dic[char] = i

        only_upper = set([x for x in word if x.isupper()])

        for char in only_upper:
            try:
                if dic[char] > dic[char.lower()]:
                    res += 1
            except:
                continue

        return res
