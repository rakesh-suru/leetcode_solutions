class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.ans = 0

        visited = [[False] * n for _ in range(m)]

        def solve(row, col):
            if row == m - 1 and col == n - 1:
                self.ans += 1
                return
            
            visited[row][col] = True
            for x, y in [(0, 1), (1, 0)]:
                r = row + x
                c = col + y

                if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                    solve(r, c)
            visited[row][col] = False
        
        solve(0, 0)
        return self.ans