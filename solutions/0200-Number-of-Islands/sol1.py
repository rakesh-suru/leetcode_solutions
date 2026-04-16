class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        ans = 0

        def bfs(i, j):
            if grid[i][j] == "0":
                return
            
            queue = deque()
            queue.append([i, j])
            visited[i][j] = True

            while queue:
                x, y = queue.popleft()
                directions = [(0,1), (0,-1), (1,0), (-1,0)]

                for dx, dy in directions:
                    r = x + dx
                    c = y + dy

                    if 0 <= r < m and 0 <= c < n:
                        if not visited[r][c] and grid[r][c] == "1":
                            visited[r][c] = True
                            queue.append([r, c])

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    bfs(i, j)
                    ans += 1
        
        return ans