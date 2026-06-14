class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def solve(idx, buy, buys, sells):
            if idx == n or sells == 0:
                return 0

            if buy:
                take = solve(idx + 1, 0, buys - 1, sells) - prices[idx]
                skip = solve(idx + 1, 1, buys, sells)
                return max(take, skip)

            else:
                sell = solve(idx + 1, 1, buys, sells - 1) + prices[idx]
                skip = solve(idx + 1, 0, buys, sells)
                return max(sell, skip)

        return solve(0, 1, 2, 2)