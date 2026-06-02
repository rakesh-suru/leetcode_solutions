class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]

        def solve(idx, total):
            if total == 0:
                return 0

            if idx == 0:
                if total % coins[idx] == 0:
                    return total // coins[idx]
                return float("inf")
            
            if dp[idx][total] != -1:
                return dp[idx][total]

            not_take = solve(idx - 1, total)

            take = float("inf")
            if coins[idx] <= total:
                take = 1 + solve(idx, total - coins[idx])

            dp[idx][total] = min(take, not_take)
            return dp[idx][total]

        ans = solve(n - 1, amount)
        return -1 if ans == float("inf") else ans