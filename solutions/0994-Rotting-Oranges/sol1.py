class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        ans = 0

        def bfs(queue):
            nonlocal ans

            while queue:
                r, c, t = queue.popleft()
                ans = max(ans, t)

                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    x, y = r + dx, c + dy

                    if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] == 1:
                        visited[x][y] = True
                        grid[x][y] = 2
                        queue.append((x, y, t + 1))

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited[i][j] = True

        bfs(queue)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return ans