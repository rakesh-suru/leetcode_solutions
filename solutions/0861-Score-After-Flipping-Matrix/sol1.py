class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        
        for j in range(n):
            ones = 0
            zeros = 0
            for i in range(m):
                if grid[i][j] == 1:
                    ones += 1
                else:
                    zeros += 1
            
            if zeros > ones:
                for i in range(m):
                    grid[i][j] ^= 1
        
        ans = 0
        for i in range(m):
            temp = 2 ** (n - 1)
            for j in range(n):
                if grid[i][j] == 1:
                    ans += temp
                temp //= 2
        
        return ans