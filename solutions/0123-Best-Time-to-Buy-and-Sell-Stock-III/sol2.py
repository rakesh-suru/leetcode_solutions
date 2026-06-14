class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def solve(idx, buy, cap):
            if idx == n or cap == 0:
                return 0

            if buy:
                return max(
                    -prices[idx] + solve(idx + 1, 0, cap),
                    solve(idx + 1, 1, cap)
                )
            else:
                return max(
                    prices[idx] + solve(idx + 1, 1, cap - 1),
                    solve(idx + 1, 0, cap)
                )

        return solve(0, 1, 2)