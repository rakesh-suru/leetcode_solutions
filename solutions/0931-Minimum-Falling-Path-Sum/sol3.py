class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = [[float("inf")] * n for _ in range(n)]

        dp[0] = matrix[0][:]

        for i in range(1, n):
            for j in range(n):

                for k in [-1, 0, 1]:
                    prev_col = j + k

                    if prev_col < 0 or prev_col >= n:
                        continue

                    dp[i][j] = min(
                        dp[i][j],
                        matrix[i][j] + dp[i - 1][prev_col]
                    )

        return min(dp[-1])