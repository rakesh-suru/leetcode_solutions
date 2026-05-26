class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[[-1] * n for _ in range(n)] for _ in range(m)]

        def solve(i, j1, j2):

            if j1 < 0 or j1 >= n or j2 < 0 or j2 >= n:
                return -float("inf")

            if i == m - 1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]

            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]

            maxi = 0

            for d1 in [-1, 0, 1]:
                for d2 in [-1, 0, 1]:

                    if j1 == j2:
                        value = grid[i][j1]
                    else:
                        value = grid[i][j1] + grid[i][j2]

                    value += solve(i + 1, j1 + d1, j2 + d2)

                    maxi = max(maxi, value)

            dp[i][j1][j2] = maxi
            return maxi

        return solve(0, 0, n - 1)