class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        minutes = 0
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                    x, y = r + dx, c + dy
                    
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        queue.append((x, y))
                        fresh -= 1
            
            minutes += 1
        
        return -1 if fresh > 0 else minutes