class Solution:
    def minCost(self, n: int) -> int:
        self.cost = 0

        def solve(num):
            if num == 1:
                return
            
            self.cost = self.cost + num - 1
            return solve(num - 1)
        
        solve(n)
        return self.cost