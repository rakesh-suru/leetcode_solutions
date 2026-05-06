class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])

        def canReach(maxEffort):
            visited = [[False] * n for _ in range(m)]
            queue = deque([(0, 0)])
            visited[0][0] = True

            while queue:
                row, col = queue.popleft()

                if row == m - 1 and col == n - 1:
                    return True

                for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                    x, y = row + dx, col + dy

                    if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                        if abs(heights[row][col] - heights[x][y]) <= maxEffort:
                            visited[x][y] = True
                            queue.append((x, y))

            return False

        left, right = 0, 10**6

        while left < right:
            mid = (left + right) // 2

            if canReach(mid):
                right = mid
            else:
                left = mid + 1

        return left