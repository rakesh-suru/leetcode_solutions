class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        ans = [[0] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        
        def bfs():
            while queue:
                r, c, d = queue.popleft()
                ans[r][c] = d
                
                for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                    x = r + dx
                    y = c + dy
                    
                    if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                        queue.append((x, y, d + 1))
                        visited[x][y] = True

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited[i][j] = True

        bfs()
        return ans