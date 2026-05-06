class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        pq = []

        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0

        heapq.heappush(pq, (0, 0, 0))

        while pq:
            dis, row, col = heapq.heappop(pq)

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                x = row + dx
                y = col + dy

                if 0 <= x < m and 0 <= y < n:
                    temp = max(dis, abs(heights[row][col] - heights[x][y]))
                    if temp < dist[x][y]:
                        dist[x][y] = temp
                        heapq.heappush(pq, (temp, x, y))
        
        return dist[m - 1][n - 1]