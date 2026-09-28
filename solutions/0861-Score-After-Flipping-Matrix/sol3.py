class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0

        for j in range(n):
            ones = 0

            for i in range(m):
                if grid[i][0] == grid[i][j]:
                    ones += 1

            ones = max(ones, m - ones)

            ans += ones * (2 ** (n - j - 1))

        return ans