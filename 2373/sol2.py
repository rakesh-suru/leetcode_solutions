class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        maxLocal = [ [ 0 for _ in range(n-2)] for _ in range(n-2)]
        for i in range(1,n-1):
            for j in range(1, n-1):
                maxLocal[i-1][j-1] = max(max(grid[i-1][j-1:j+2]), max(grid[i][j-1:j+2]), max(grid[i+1][j-1:j+2]))
        return maxLocal