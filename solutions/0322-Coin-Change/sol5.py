class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        INF = float("inf")

        prev = [INF] * (amount + 1)

        for t in range(amount + 1):
            if t % coins[0] == 0:
                prev[t] = t // coins[0]

        for idx in range(1, n):
            curr = [INF] * (amount + 1)

            for total in range(amount + 1):
                not_take = prev[total]

                take = INF
                if coins[idx] <= total:
                    take = 1 + curr[total - coins[idx]]

                curr[total] = min(take, not_take)

            prev = curr

        return -1 if prev[amount] == INF else prev[amount]