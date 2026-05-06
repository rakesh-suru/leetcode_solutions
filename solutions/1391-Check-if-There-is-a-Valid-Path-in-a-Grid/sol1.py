class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]
        ans = False

        def can_move(curr, nxt, dr, dc):
            if dr == 0 and dc == 1:
                return nxt in [1, 3, 5]
            if dr == 0 and dc == -1:
                return nxt in [1, 4, 6]
            if dr == 1 and dc == 0:
                return nxt in [2, 5, 6]
            if dr == -1 and dc == 0:
                return nxt in [2, 3, 4]
            return False

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

            if grid[row][col] == 1:
                for dr, dc in [(0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and can_move(1, grid[nr][nc], dr, dc):
                        dfs(nr, nc)

            elif grid[row][col] == 2:
                for dr, dc in [(1, 0), (-1, 0)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and can_move(2, grid[nr][nc], dr, dc):
                        dfs(nr, nc)

            elif grid[row][col] == 3:
                for dr, dc in [(0, -1), (1, 0)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and can_move(3, grid[nr][nc], dr, dc):
                        dfs(nr, nc)

            elif grid[row][col] == 4:
                for dr, dc in [(0, 1), (1, 0)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and can_move(4, grid[nr][nc], dr, dc):
                        dfs(nr, nc)

            elif grid[row][col] == 5:
                for dr, dc in [(0, -1), (-1, 0)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and can_move(5, grid[nr][nc], dr, dc):
                        dfs(nr, nc)

            elif grid[row][col] == 6:
                for dr, dc in [(0, 1), (-1, 0)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and can_move(6, grid[nr][nc], dr, dc):
                        dfs(nr, nc)

        dfs(0, 0)
        return ans