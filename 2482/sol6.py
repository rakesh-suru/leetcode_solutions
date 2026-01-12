class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        a=[grid[i].count(1)-grid[i].count(0) for i in range(m)]
        b=[]
        for j in range(n):
            ones = sum(grid[i][j] for i in range(m))
            zeros = m - ones
            b.append(ones - zeros)
        for i in range(m):
            for j in range(n):
                grid[i][j]=a[i]+b[j]
        return grid