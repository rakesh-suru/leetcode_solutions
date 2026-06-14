class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[-1] * 2 for _ in range(n)]

        def solve(idx, buy):
            if idx >= n:
                return 0
            
            if dp[idx][buy] != -1:
                return dp[idx][buy]

            if buy:
                dp[idx][buy] = max(solve(idx + 1, 0) - prices[idx], solve(idx + 1, 1))
                return dp[idx][buy]
                
            dp[idx][buy] = max(solve(idx + 2, 1) + prices[idx], solve(idx + 1, 0))
            return dp[idx][buy]
        
        return solve(0, 1)