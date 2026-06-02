class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        INF = float("inf")

        dp = [[INF] * (amount + 1) for _ in range(n)]

        for t in range(amount + 1):
            if t % coins[0] == 0:
                dp[0][t] = t // coins[0]

        for idx in range(1, n):
            for total in range(amount + 1):
                not_take = dp[idx - 1][total]

                take = INF
                if coins[idx] <= total:
                    take = 1 + dp[idx][total - coins[idx]]

                dp[idx][total] = min(take, not_take)

        ans = dp[n - 1][amount]
        return -1 if ans == INF else ans