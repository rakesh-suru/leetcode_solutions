class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = m * 2 ** (n - 1)

        for j in range(1, n):
            ones = 0

            for i in range(m):
                if grid[i][j] != grid[i][0]:
                    ones += 1

            ones = max(ones, m - ones)

            ans += ones * (2 ** (n - j - 1))

        return ans