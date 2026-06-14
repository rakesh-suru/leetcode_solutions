class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ahead_buy = 0
        ahead_sell = 0

        for idx in range(len(prices) - 1, -1, -1):
            curr_buy = max(
                -prices[idx] + ahead_sell,
                ahead_buy
            )

            curr_sell = max(
                prices[idx] + ahead_buy,
                ahead_sell
            )

            ahead_buy = curr_buy
            ahead_sell = curr_sell

        return ahead_buy