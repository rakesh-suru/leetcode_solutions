class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        empty = 0
        start_r = start_c = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    empty += 1
                if grid[i][j] == 1:
                    start_r, start_c = i, j
        
        visited = [[False]*n for _ in range(m)]
        ans = 0
        
        def dfs(r, c, count):
            nonlocal ans
            
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            
            if grid[r][c] == -1 or visited[r][c]:
                return
            
            if grid[r][c] == 2:
                if count == empty:
                    ans += 1
                return
            
            visited[r][c] = True
            
            dfs(r+1, c, count+1)
            dfs(r-1, c, count+1)
            dfs(r, c+1, count+1)
            dfs(r, c-1, count+1)
            
            visited[r][c] = False
        
        dfs(start_r, start_c, 1)
        
        return ans
