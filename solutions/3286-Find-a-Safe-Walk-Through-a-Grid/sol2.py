class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        visited = [[False] * n for _ in range(m)]

        def dfs(i, j, h):
            h -= grid[i][j]

            if h <= 0:
                return False

            if i == m - 1 and j == n - 1:
                return True

            visited[i][j] = True

            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x, y = i + dx, j + dy

                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if dfs(x, y, h):
                        return True

            visited[i][j] = False
            return False

        return dfs(0, 0, health)