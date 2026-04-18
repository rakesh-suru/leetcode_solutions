class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        queue = deque()

        def bfs():
            while queue:
                r, c = queue.popleft()
                visited[r][c] = True

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x = r + dx
                    y = c + dy

                    if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] == 1:
                        queue.append((x, y))
                        visited[x][y] = True
        
        for col in range(n):
            if grid[0][col] == 1:
                queue.append((0, col))
            if grid[m - 1][col] == 1:
                queue.append((m - 1, col))
        
        for row in range(m):
            if grid[row][0] == 1:
                queue.append((row, 0))
            if grid[row][n - 1] == 1:
                queue.append((row, n - 1))

        bfs()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    ans += 1
        
        return ans
