class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        if s == "":
            return 0

        for i in range(n):
            dp[i][i] = True
            ans += 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        ans += 1
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        ans += 1
        return ans


newSol = Solution()
string = 'aaaaa'
print(newSol.countSubstrings(string))
