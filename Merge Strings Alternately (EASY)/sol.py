class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)
        s = ""
        if length1 <= length2:
            for i in range(length1):
                s += word1[i] + word2[i]
            s += word2[length1:]
            return s
        else:
            for i in range(length2):
                s += word1[i] + word2[i]
            s += word1[length2:]
            return s


sol = Solution()
word1 = "abcd"
word2 = "pq"
print(sol.mergeAlternately(word1, word2))
