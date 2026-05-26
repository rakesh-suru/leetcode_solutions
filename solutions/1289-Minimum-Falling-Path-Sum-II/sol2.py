class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dp = [[0] * n for _ in range(n)]

        for col in range(n):
            dp[n - 1][col] = grid[n - 1][col]

        for row in range(n - 2, -1, -1):

            for col in range(n):

                temp = float("inf")

                for next_col in range(n):

                    if next_col != col:
                        temp = min(temp, dp[row + 1][next_col])

                dp[row][col] = grid[row][col] + temp

        return min(dp[0])