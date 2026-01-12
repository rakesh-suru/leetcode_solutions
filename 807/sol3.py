class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        grid_len = len(grid)
        col_len = len(grid[0])
        row_max = [0] * grid_len
        col_max = [0] * col_len

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                row_max[i] = max(row_max[i], grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])

        ans = 0
        for i in range(grid_len):
            for j in range(col_len):
                ans += min(row_max[i], col_max[j]) - grid[i][j]
        
        return ans