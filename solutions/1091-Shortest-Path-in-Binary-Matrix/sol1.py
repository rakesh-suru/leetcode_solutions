class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        dist = [[float("inf")] * n for _ in range(n)]
        queue = deque()

        dist[0][0] = 1
        queue.append((0, 0, 1))

        if grid[0][0] == 1:
            return -1

        while queue:
            row, col, d = queue.popleft()

            if row == n - 1 and col == n - 1:
                return dist[row][col]
            
            for x, y in [(-1, -1), (0, -1), (-1, 0), (1, -1), (-1, 1), (0, 1), (1, 0), (1, 1)]:
                r = row + x
                c = col + y

                if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                    if d + 1 < dist[r][c]:
                        dist[r][c] = d + 1
                        queue.append((r, c, d + 1))
        
        return -1