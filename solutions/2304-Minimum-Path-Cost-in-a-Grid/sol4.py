class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        next_row = grid[-1][:]

        for row in range(m - 2, -1, -1):

            curr = [0] * n

            for col in range(n):

                value = grid[row][col]

                curr[col] = min(
                    grid[row][col] +
                    moveCost[value][next_col] +
                    next_row[next_col]
                    for next_col in range(n)
                )

            next_row = curr

        return min(next_row)