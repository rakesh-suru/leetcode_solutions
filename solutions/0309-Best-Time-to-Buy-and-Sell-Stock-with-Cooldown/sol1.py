class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def solve(idx, buy):
            if idx >= n:
                return 0
            
            if buy:
                return max(solve(idx + 1, 0) - prices[idx], solve(idx + 1, 1))
                
            return max(solve(idx + 2, 1) + prices[idx], solve(idx + 1, 0))
        
        return solve(0, 1)