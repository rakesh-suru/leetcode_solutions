class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float("inf")
        grid = [[INF] * n for _ in range(n)]

        for i in range(n):
            grid[i][i] = 0
        
        for u, v, w in edges:
            grid[u][v] = w
            grid[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if grid[i][k] == INF or grid[k][j] == INF:
                        continue
                    if grid[i][j] > grid[i][k] + grid[k][j]:
                        grid[i][j] = grid[i][k] + grid[k][j]
        
        max_cities = float("inf")
        city = -1
        for i, row in enumerate(grid):
            temp = 0
            for val in row:
                if val <= distanceThreshold:
                    temp += 1
            if temp <= max_cities:
                max_cities = temp
                city = i
        
        return city