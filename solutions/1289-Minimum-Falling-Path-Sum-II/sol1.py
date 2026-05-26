class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dp = [[None] * n for _ in range(n)]

        def solve(row, col):

            if row == n - 1:
                return grid[row][col]

            if dp[row][col] is not None:
                return dp[row][col]

            temp = float("inf")

            for next_col in range(n):

                if next_col != col:
                    temp = min(
                        temp,
                        solve(row + 1, next_col)
                    )

            dp[row][col] = grid[row][col] + temp

            return dp[row][col]

        ans = float("inf")

        for i in range(n):
            ans = min(ans, solve(0, i))

        return ans