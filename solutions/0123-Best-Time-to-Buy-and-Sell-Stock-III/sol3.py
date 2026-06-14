class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}

        def solve(idx, buy, cap):
            if idx == n or cap == 0:
                return 0

            if (idx, buy, cap) in dp:
                return dp[(idx, buy, cap)]

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

            dp[(idx, buy, cap)] = ans
            return ans

        return solve(0, 1, 2)