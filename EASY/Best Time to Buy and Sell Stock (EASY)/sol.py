class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < cheapest:
                cheapest = price
            max_profit = max(max_profit, price - cheapest)

        return max_profit
