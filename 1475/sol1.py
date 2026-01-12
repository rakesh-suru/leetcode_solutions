class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        for i in range(n):
            ans[i] = prices[i]
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    ans[i] = prices[i] - prices[j]
                    break
        return ans
