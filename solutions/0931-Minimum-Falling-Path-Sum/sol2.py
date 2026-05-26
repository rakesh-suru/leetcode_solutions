class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = [[None] * n for _ in range(n)]

        def solve(row, col):

            if col < 0 or col >= n:
                return float("inf")

            if row == n - 1:
                return matrix[row][col]

            if dp[row][col] is not None:
                return dp[row][col]

            down_left = solve(row + 1, col - 1)
            down = solve(row + 1, col)
            down_right = solve(row + 1, col + 1)

            dp[row][col] = matrix[row][col] + min(
                down_left,
                down,
                down_right
            )

            return dp[row][col]

        ans = float("inf")

        for i in range(n):
            ans = min(ans, solve(0, i))

        return ans