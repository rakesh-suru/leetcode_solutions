class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        q = deque()

        for row in grid:
            q.extend(row)

        q.rotate(k)

        for i in range(m):
            for j in range(n):
                grid[i][j] = q.popleft()

        return grid