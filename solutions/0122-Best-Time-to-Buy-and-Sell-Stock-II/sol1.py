class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)

        def solve(idx, buy, total):
            nonlocal ans
            if idx == n:
                ans = max(ans, total)
                return
            
            if buy:
                solve(idx + 1, 0, total - prices[idx])
                solve(idx + 1, 1, total)
            
            else:
                solve(idx + 1, 1, total + prices[idx])
                solve(idx + 1, 0, total)
        
        solve(0, 1, 0)
        return ans