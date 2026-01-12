class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]

        total = 0
        for r in range(n):
            for c in range(n):
                total += min(row_max[r], col_max[c]) - grid[r][c]
        
        return total