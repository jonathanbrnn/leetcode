class Solution:
    def convert(self, word: str) -> str:
        i = 0
        patt = []
        dic = {}

        for char in word:
            if char not in dic:
                dic[char] = str(i)
                i += 1
            patt.append(dic[char])

        return patt

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        patt = self.convert(pattern)

        for word in words:
            if patt == self.convert(word):
                res.append(word)

        return res
