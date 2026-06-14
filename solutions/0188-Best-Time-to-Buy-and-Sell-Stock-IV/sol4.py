class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        ahead = [[0] * (k + 1) for _ in range(2)]

        for idx in range(n - 1, -1, -1):
            curr = [[0] * (k + 1) for _ in range(2)]

            for buy in range(2):
                for cap in range(1, k + 1):
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

        return ahead[1][k]