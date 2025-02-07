class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_buy = prices[0]
        profit = 0

        for price in prices[1:]:
            min_buy = min(min_buy, price)
            profit = max(profit, price - min_buy)

        return profit
            