class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)

        for i in range(n - 1):
            buy = prices[i]
            for j in range(i + 1, n):
                ans = max(ans, prices[j] - buy)
        
        return ans