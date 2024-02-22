class Solution:
    def findJudge(self, n: int, trust: list) -> int:
        trust_counts = [0] * (n + 1)
        for i, j in trust:
            trust_counts[i] -= 1
            trust_counts[j] += 1
        for i in range(1, n + 1):
            if trust_counts[i] == n - 1:
                return i
        return -1


n = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

sol = Solution()
print(sol.findJudge(n, trust))
