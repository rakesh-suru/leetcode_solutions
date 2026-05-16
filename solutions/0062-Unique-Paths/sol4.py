class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def solve(row, col):
            if row == 0 and col == 0:
                return 1
            
            elif row < 0 or col < 0:
                return 0
            
            up = solve(row, col - 1)
            left = solve(row - 1, col)
            return up + left
        
        return solve(m - 1, n - 1)