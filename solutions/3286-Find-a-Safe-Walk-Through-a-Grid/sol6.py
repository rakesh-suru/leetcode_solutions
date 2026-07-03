class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        INF = float("inf")
        dist = [[INF] * n for _ in range(m)]

        dist[0][0] = grid[0][0]
        dq = deque([(0, 0)])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while dq:
            i, j = dq.popleft()

            for dx, dy in directions:
                x, y = i + dx, j + dy

                if 0 <= x < m and 0 <= y < n:
                    new_cost = dist[i][j] + grid[x][y]

                    if new_cost < dist[x][y]:
                        dist[x][y] = new_cost

                        if grid[x][y] == 0:
                            dq.appendleft((x, y))
                        else:
                            dq.append((x, y))

        return dist[m - 1][n - 1] < health