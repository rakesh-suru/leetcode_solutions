class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        visited = [[False] * n for _ in range(m)]

        dp = [[[-1] * (health + 1) for _ in range(n)] for _ in range(m)]

        def dfs(i, j, h):
            h -= grid[i][j]

            if h <= 0:
                return False

            if i == m - 1 and j == n - 1:
                return True

            if dp[i][j][h] != -1:
                return dp[i][j][h]

            visited[i][j] = True

            ans = False

            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                x, y = i + dx, j + dy

                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if dfs(x, y, h):
                        ans = True
                        break

            visited[i][j] = False

            dp[i][j][h] = ans
            return ans

        return dfs(0, 0, health)