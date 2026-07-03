from heapq import heappush, heappop

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        pq = [(grid[0][0], 0, 0)]

        while pq:
            cost, i, j = heappop(pq)

            if cost > dist[i][j]:
                continue

            if i == m - 1 and j == n - 1:
                return cost < health

            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x, y = i + dx, j + dy

                if 0 <= x < m and 0 <= y < n:
                    nc = cost + grid[x][y]

                    if nc < dist[x][y]:
                        dist[x][y] = nc
                        heappush(pq, (nc, x, y))

        return False