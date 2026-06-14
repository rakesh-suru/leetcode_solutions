class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        dp = [[0] * 2 for _ in range(n + 1)]

        for idx in range(n - 1, -1, -1):
            dp[idx][1] = max(
                -prices[idx] + dp[idx + 1][0],
                dp[idx + 1][1]
            )

            dp[idx][0] = max(
                prices[idx] + dp[idx + 1][1] - fee,
                dp[idx + 1][0]
            )

        return dp[0][1]