class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        start = health - grid[0][0]
        if start <= 0:
            return False

        best = [[-1] * n for _ in range(m)]
        best[0][0] = start

        q = deque([(0, 0, start)])

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while q:
            i, j, h = q.popleft()

            if i == m - 1 and j == n - 1:
                return True

            for dx, dy in directions:
                x, y = i + dx, j + dy

                if 0 <= x < m and 0 <= y < n:
                    nh = h - grid[x][y]

                    if nh > 0 and nh > best[x][y]:
                        best[x][y] = nh
                        q.append((x, y, nh))

        return False