class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        front = [[0] * n for _ in range(n)]

        for j1 in range(n):
            for j2 in range(n):

                if j1 == j2:
                    front[j1][j2] = grid[m - 1][j1]
                else:
                    front[j1][j2] = grid[m - 1][j1] + grid[m - 1][j2]

        for i in range(m - 2, -1, -1):

            curr = [[0] * n for _ in range(n)]

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

                                value += front[nj1][nj2]

                                maxi = max(maxi, value)

                    curr[j1][j2] = maxi

            front = curr

        return front[0][n - 1]