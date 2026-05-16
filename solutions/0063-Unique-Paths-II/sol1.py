class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        def solve(row, col):

            if obstacleGrid[row][col] == 1:
                return 0

            elif row == 0 and col == 0:
                return 1
            
            elif row < 0 or col < 0:
                return 0
            
            up = solve(row, col - 1)
            left = solve(row - 1, col)
            return up + left
        
        return solve(m - 1, n - 1)