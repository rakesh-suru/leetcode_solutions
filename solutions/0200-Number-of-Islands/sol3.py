class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    
                    queue = deque()
                    queue.append((i, j))
                    grid[i][j] = "0"

                    while queue:
                        x, y = queue.popleft()

                        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                            r, c = x + dx, y + dy

                            if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
                                grid[r][c] = "0"
                                queue.append((r, c))

        return ans