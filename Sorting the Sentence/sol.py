class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        res = [0] * len(s)

        for word in s:
            res[int(word[-1]) - 1] = word[:len(word) - 1]

        return " ".join(res)


print(Solution().sortSentence("sentence4 a3 is2 This1"))
