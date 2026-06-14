class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = [0, 0]

        for idx in range(len(prices) - 1, -1, -1):
            curr = [0, 0]

            curr[1] = max(
                -prices[idx] + prev[0],
                prev[1]
            )

            curr[0] = max(
                prices[idx] + prev[1],
                prev[0]
            )

            prev = curr

        return prev[1]