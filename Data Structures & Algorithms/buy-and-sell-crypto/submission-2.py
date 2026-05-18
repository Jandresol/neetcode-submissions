class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_day = 0
        for sell_day in range(1, len(prices)):
            if prices[buy_day] > prices[sell_day]:
                buy_day = sell_day
            profit = prices[sell_day] - prices[buy_day]
            max_profit = max(profit, max_profit)
        return max_profit
        