class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[-1] * (amount + 1) for _ in range(n)]

        def solve(idx, total):
            if total == amount:
                return 1

            if total > amount or idx == n:
                return 0

            if dp[idx][total] != -1:
                return dp[idx][total]

            take = solve(idx, total + coins[idx])
            not_take = solve(idx + 1, total)

            dp[idx][total] = take + not_take
            return dp[idx][total]

        return solve(0, 0)