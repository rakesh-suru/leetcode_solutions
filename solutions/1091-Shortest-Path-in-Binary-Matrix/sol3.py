from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        dist = [[float("inf")] * n for _ in range(n)]
        
        directions = [(-1,-1), (0,-1), (-1,0), (1,-1),
                      (-1,1), (0,1), (1,0), (1,1)]
        
        def dfs(r, c, d):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] == 1:
                return

            if d >= dist[r][c]:
                return

            dist[r][c] = d

            for dr, dc in directions:
                dfs(r + dr, c + dc, d + 1)
        
        dfs(0, 0, 1)
        
        return dist[n-1][n-1] if dist[n-1][n-1] != float("inf") else -1