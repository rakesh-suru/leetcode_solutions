class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue

                queue = deque()
                queue.append((i, j, -1, -1))
                visited[i][j] = True

                while queue:
                    r, c, pr, pc = queue.popleft()

                    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == grid[r][c]:
                            
                            if not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc, r, c))
                            
                            elif (nr, nc) != (pr, pc):
                                return True
        
        return False