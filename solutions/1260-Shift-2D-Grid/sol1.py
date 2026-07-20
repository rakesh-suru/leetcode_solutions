class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k % (m * n)

        temp = [num for row in grid for num in row]
        temp = temp[-k:] + temp[:-k]
        cnt = 0

        for i in range(m):
            for j in range(n):
                grid[i][j] = temp[cnt]
                cnt += 1
        
        return grid