class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [float('-inf')] * 4

        for price in prices:
            dp[0] = max(dp[0], -price)
            dp[1] = max(dp[1], dp[0] + price)
            dp[2] = max(dp[2], dp[1] - price)
            dp[3] = max(dp[3], dp[2] + price)
            
        return max(0, dp[3])