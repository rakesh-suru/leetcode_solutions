class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def goDown(i, j):

            if i >= n or j >= n or grid[i][j] == -1:
                return -float("inf")

            if i == n - 1 and j == n - 1:

                cherry = grid[i][j]
                grid[i][j] = 0

                res = cherry + goUp(n - 1, n - 1)

                grid[i][j] = cherry

                return res

            cherry = grid[i][j]

            grid[i][j] = 0

            down = goDown(i + 1, j)
            right = goDown(i, j + 1)

            grid[i][j] = cherry

            return cherry + max(down, right)

        def goUp(i, j):

            if i < 0 or j < 0 or grid[i][j] == -1:
                return -float("inf")

            if i == 0 and j == 0:
                return grid[i][j]

            cherry = grid[i][j]

            grid[i][j] = 0

            up = goUp(i - 1, j)
            left = goUp(i, j - 1)

            grid[i][j] = cherry

            return cherry + max(up, left)

        ans = goDown(0, 0)

        return max(ans, 0)