class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        from functools import lru_cache

        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(i, j, h):

            h -= grid[i][j]

            if h <= 0:
                return False

            if i == m - 1 and j == n - 1:
                return True

            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x, y = i + dx, j + dy

                if 0 <= x < m and 0 <= y < n:
                    if dfs(x, y, h):
                        return True

            return False

        return dfs(0,0,health)