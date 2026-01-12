class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        total_to_visit = 0
        start_r = start_c = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    total_to_visit += 1
                if grid[i][j] == 1:
                    start_r, start_c = i, j
        
        def dfs(r: int, c: int, visited_count: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == -1:
                return 0
            
            if grid[r][c] == 2:
                return 1 if visited_count == total_to_visit else 0
            
            temp = grid[r][c]
            grid[r][c] = -1
            
            paths = 0
            paths += dfs(r + 1, c, visited_count + 1)
            paths += dfs(r - 1, c, visited_count + 1)
            paths += dfs(r, c + 1, visited_count + 1)
            paths += dfs(r, c - 1, visited_count + 1)
            
            grid[r][c] = temp
            return paths
        
        return dfs(start_r, start_c, 1)
