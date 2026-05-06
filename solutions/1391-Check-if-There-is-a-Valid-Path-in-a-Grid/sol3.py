from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        visited = set()
        queue = deque([(0, 0)])
        visited.add((0, 0))

        while queue:
            row, col = queue.popleft()

            if row == m - 1 and col == n - 1:
                return True

            for dr, dc in directions[grid[row][col]]:
                nr, nc = row + dr, col + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        return False