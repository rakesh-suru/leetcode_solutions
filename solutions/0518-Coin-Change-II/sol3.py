class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[-1] * (amount + 1) for _ in range(n)]

        def solve(idx, rem):
            if rem == 0:
                return 1

            if idx == n or rem < 0:
                return 0

            if dp[idx][rem] != -1:
                return dp[idx][rem]

            take = solve(idx, rem - coins[idx])
            not_take = solve(idx + 1, rem)

            dp[idx][rem] = take + not_take
            return dp[idx][rem]

        return solve(0, amount)