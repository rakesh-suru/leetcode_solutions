class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        def solve(idx, total):
            if total == 0:
                return 0

            if idx == -1:
                return float("inf")

            not_take = solve(idx - 1, total)

            take = float("inf")
            if coins[idx] <= total:
                take = 1 + solve(idx, total - coins[idx])

            return min(take, not_take)

        ans = solve(n - 1, amount)
        return -1 if ans == float("inf") else ans