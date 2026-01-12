class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        row_ones = [0] * m
        col_ones = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_ones[i] += 1
                    col_ones[j] += 1

        diff = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ones  = row_ones[i] + col_ones[j]
                zeros = (n - row_ones[i]) + (m - col_ones[j])
                diff[i][j] = ones-zeros
        
        return diff