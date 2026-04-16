class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while queue:
            r, c = queue.popleft()
            
            for dx, dy in directions:
                x, y = r + dx, c + dy
                
                if 0 <= x < m and 0 <= y < n:
                    if mat[x][y] > mat[r][c] + 1:
                        mat[x][y] = mat[r][c] + 1
                        queue.append((x, y))

        return mat