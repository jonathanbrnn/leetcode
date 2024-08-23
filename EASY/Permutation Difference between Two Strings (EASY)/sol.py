class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dic = {}
        res = 0

        for i, char in enumerate(s):
            dic[char] = i

        for i, char in enumerate(t):
            res += abs(dic[char] - i)

        return res
