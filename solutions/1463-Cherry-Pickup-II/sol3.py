class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[[0] * n for _ in range(n)] for _ in range(m)]

        for j1 in range(n):
            for j2 in range(n):
                if j1 == j2:
                    dp[m - 1][j1][j2] = grid[m - 1][j1]
                else:
                    dp[m - 1][j1][j2] = grid[m - 1][j1] + grid[m - 1][j2]

        for i in range(m - 2, -1, -1):

            for j1 in range(n):
                for j2 in range(n):

                    maxi = -float("inf")

                    for d1 in [-1, 0, 1]:
                        for d2 in [-1, 0, 1]:

                            nj1 = j1 + d1
                            nj2 = j2 + d2

                            if 0 <= nj1 < n and 0 <= nj2 < n:

                                if j1 == j2:
                                    value = grid[i][j1]
                                else:
                                    value = grid[i][j1] + grid[i][j2]

                                value += dp[i + 1][nj1][nj2]

                                maxi = max(maxi, value)

                    dp[i][j1][j2] = maxi

        return dp[0][0][n - 1]