class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        left = 0
        right = 1
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            profit = prices[right] - prices[left]
            ans = max(profit, ans)
        return ans
        