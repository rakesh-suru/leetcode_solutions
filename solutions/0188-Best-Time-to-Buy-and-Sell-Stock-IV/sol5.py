class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        ahead = [0] * (2 * k + 1)

        for idx in range(n - 1, -1, -1):
            curr = [0] * (2 * k + 1)

            for tranNo in range(2 * k - 1, -1, -1):

                if tranNo % 2 == 0:
                    curr[tranNo] = max(
                        -prices[idx] + ahead[tranNo + 1],
                        ahead[tranNo]
                    )
                else:
                    curr[tranNo] = max(
                        prices[idx] + ahead[tranNo + 1],
                        ahead[tranNo]
                    )

            ahead = curr

        return ahead[0]