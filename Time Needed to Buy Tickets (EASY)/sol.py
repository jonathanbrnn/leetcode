class Solution:
    def timeRequiredToBuy(self, tickets: list, k: int) -> int:
        res = 0

        for i, ticket in enumerate(tickets):
            if i <= k:
                res += min(ticket, tickets[k])
            else:
                res += min(ticket, tickets[k] - 1)
        return res


tickets = [2,3,2]
k = 2
print(Solution().timeRequiredToBuy(tickets, k))
