from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        queue = deque([(0, 0, 1)])
        visited = set()
        visited.add((0, 0))
        
        directions = [(-1,-1), (0,-1), (-1,0), (1,-1),
                      (-1,1), (0,1), (1,0), (1,1)]
        
        while queue:
            row, col, d = queue.popleft()
            
            if row == n - 1 and col == n - 1:
                return d
            
            for dx, dy in directions:
                r, c = row + dx, col + dy
                
                if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c, d + 1))
        
        return -1