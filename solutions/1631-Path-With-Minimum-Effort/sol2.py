import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])

        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]

        while pq:
            dis, row, col = heapq.heappop(pq)

            if dis > dist[row][col]:
                continue

            if row == m - 1 and col == n - 1:
                return dis

            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                x, y = row + dx, col + dy

                if 0 <= x < m and 0 <= y < n:
                    temp = max(dis, abs(heights[row][col] - heights[x][y]))

                    if temp < dist[x][y]:
                        dist[x][y] = temp
                        heapq.heappush(pq, (temp, x, y))

        return dist[m - 1][n - 1]