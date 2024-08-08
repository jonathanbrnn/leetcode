# Credit to https://www.geeksforgeeks.org/introduction-to-levenshtein-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        if n == 0:
            return m
        if m == 0:
            return n

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[m][n]


print(Solution().minDistance("intention", "execution"))
