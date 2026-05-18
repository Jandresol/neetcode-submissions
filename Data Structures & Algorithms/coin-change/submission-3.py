class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # trying to determine how many coins to use
        # recursive problem, can go through every coin combination and minimixe it
        # test case
        # dp[7] = 1 + dp[2] if coin = 5
        # dp array tracks number of coins used to get to an amount
        # dp[amount] = min(dp[amount], 1+ dp[amount - coin])
        # initialize dp array with maximum
        dp = [1e9] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for a in range(1, amount + 1):
                if a-c >= 0:
                    dp[a] = min(dp[a], 1+ dp[a - c])
        print(dp) 
        return dp[amount] if dp[amount] != 1e9 else -1