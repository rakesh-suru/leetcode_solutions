class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        ans = [[0] * n for _ in range(m)]

        total = m * n

        for i in range(m):
            for j in range(n):
                newIndex = (i * n + j + k) % total
                r = newIndex // n
                c = newIndex % n
                ans[r][c] = grid[i][j]

        return ans