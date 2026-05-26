class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for col in range(n):
            dp[m - 1][col] = grid[m - 1][col]

        for row in range(m - 2, -1, -1):

            for col in range(n):

                ans = float('inf')

                current = grid[row][col]

                for next_col in range(n):

                    cost = (
                        grid[row][col] +
                        moveCost[current][next_col] +
                        dp[row + 1][next_col]
                    )

                    ans = min(ans, cost)

                dp[row][col] = ans

        return min(dp[0])