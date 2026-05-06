class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]
        ans = False

        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        def is_valid(curr, next_cell, dr, dc):
            return (-dr, -dc) in directions[next_cell]

        def dfs(row, col):
            nonlocal ans

            if row == m - 1 and col == n - 1:
                ans = True
                return
            
            if not (0 <= row < m and 0 <= col < n):
                return
            
            if visited[row][col]:
                return
            
            visited[row][col] = True

            for dr, dc in directions[grid[row][col]]:
                nr, nc = row + dr, col + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if not visited[nr][nc] and is_valid(grid[row][col], grid[nr][nc], dr, dc):
                        dfs(nr, nc)

        dfs(0, 0)
        return ans