class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        res = []
        a = "a"

        for word in sentence.split(" "):
            first = word[0]
            if first in vowels:
                res.append(word + "ma" + a)
            else:
                res.append(word[1:] + first + "ma" + a)
            a += "a"

        return " ".join(res)
