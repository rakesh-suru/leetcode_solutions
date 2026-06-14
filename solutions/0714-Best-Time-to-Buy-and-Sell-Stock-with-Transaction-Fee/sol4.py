class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ahead = [0, 0]

        for idx in range(len(prices) - 1, -1, -1):
            curr = [0, 0]

            curr[1] = max(
                -prices[idx] + ahead[0],
                ahead[1]
            )

            curr[0] = max(
                prices[idx] - fee + ahead[1],
                ahead[0]
            )

            ahead = curr

        return ahead[1]