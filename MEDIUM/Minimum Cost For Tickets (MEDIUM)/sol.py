class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        max_day = max(days_set)
        dp = [0] * (max_day + 1)

        for i in range(1, max_day + 1):
            if i in days_set:
                one = dp[i - 1] + costs[0]
                seven = dp[i - 7] + costs[1] if i >= 7 else costs[1]
                thirty = dp[i - 30] + costs[2] if i >= 30 else costs[2]
                dp[i] = min(one, seven, thirty)
            else:
                dp[i] = dp[i - 1]

        return dp[max_day]
