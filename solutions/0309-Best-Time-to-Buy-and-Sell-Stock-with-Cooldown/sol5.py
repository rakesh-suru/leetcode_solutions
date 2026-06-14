class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        ahead1 = [0, 0]
        ahead2 = [0, 0]

        for idx in range(n - 1, -1, -1):
            curr = [0, 0]

            curr[1] = max(
                -prices[idx] + ahead1[0],
                ahead1[1]
            )

            curr[0] = max(
                prices[idx] + ahead2[1],
                ahead1[0]
            )

            ahead2 = ahead1
            ahead1 = curr

        return ahead1[1]