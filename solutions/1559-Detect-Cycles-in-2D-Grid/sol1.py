class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(r, c, pr, pc):
            if visited[r][c]:
                return True
            
            visited[r][c] = True

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == grid[r][c]:
                        if nr == pr and nc == pc:
                            continue
                        
                        if dfs(nr, nc, r, c):
                            return True
            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):
                        return True

        return False