class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        row_max = [0] * len(grid)
        col_max = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                row_max[i] = max(row_max[i], grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += min(row_max[i], col_max[j]) - grid[i][j]
        
        return ans