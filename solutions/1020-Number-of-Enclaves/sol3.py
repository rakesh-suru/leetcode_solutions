from collections import deque
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()

        for i in range(m):
            if grid[i][0] == 1:
                queue.append((i, 0))
                grid[i][0] = 0
            if grid[i][n - 1] == 1:
                queue.append((i, n - 1))
                grid[i][n - 1] = 0

        for j in range(n):
            if grid[0][j] == 1:
                queue.append((0, j))
                grid[0][j] = 0
            if grid[m - 1][j] == 1:
                queue.append((m - 1, j))
                grid[m - 1][j] = 0

        while queue:
            r, c = queue.popleft()

            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                x, y = r + dx, c + dy

                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 0
                    queue.append((x, y))

        return sum(cell == 1 for row in grid for cell in row)