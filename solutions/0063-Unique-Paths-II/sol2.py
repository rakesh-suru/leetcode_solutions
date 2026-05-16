class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1] * n for _ in range(m)]
        
        def solve(row, col):

            if obstacleGrid[row][col] == 1:
                return 0

            elif row == 0 and col == 0:
                return 1
            
            elif row < 0 or col < 0:
                return 0
            
            if dp[row][col] != -1:
                return dp[row][col]

            up = solve(row, col - 1)
            left = solve(row - 1, col)

            dp[row][col] = up + left
            return dp[row][col]
            
        return solve(m - 1, n - 1)