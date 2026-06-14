class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1] * (k + 1) for _ in range(2)] for _ in range(n)]

        def solve(idx, buy, cap):
            if idx == n or cap == 0:
                return 0

            if dp[idx][buy][cap] != -1:
                return dp[idx][buy][cap]

            if buy:
                ans = max(
                    -prices[idx] + solve(idx + 1, 0, cap),
                    solve(idx + 1, 1, cap)
                )
            else:
                ans = max(
                    prices[idx] + solve(idx + 1, 1, cap - 1),
                    solve(idx + 1, 0, cap)
                )

            dp[idx][buy][cap] = ans
            return ans

        return solve(0, 1, k)