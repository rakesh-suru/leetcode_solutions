class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ahead = [[0] * 3 for _ in range(2)]

        for idx in range(len(prices) - 1, -1, -1):
            curr = [[0] * 3 for _ in range(2)]

            for buy in range(2):
                for cap in range(1, 3):
                    if buy:
                        curr[buy][cap] = max(
                            -prices[idx] + ahead[0][cap],
                            ahead[1][cap]
                        )
                    else:
                        curr[buy][cap] = max(
                            prices[idx] + ahead[1][cap - 1],
                            ahead[0][cap]
                        )

            ahead = curr

        return ahead[1][2]