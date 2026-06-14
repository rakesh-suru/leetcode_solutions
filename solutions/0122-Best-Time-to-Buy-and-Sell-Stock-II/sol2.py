class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def solve(idx, buy, total):
            if idx == n:
                return 0
            
            if buy:
                return max(solve(idx + 1, 0, total) - prices[idx], solve(idx + 1, 1, total))
                
            else:
                return max(solve(idx + 1, 1, total) + prices[idx], solve(idx + 1, 0, total))
        
        return solve(0, 1, 0)