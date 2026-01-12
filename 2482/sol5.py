class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        a=[grid[i].count(1)-grid[i].count(0) for i in range(m)]
        b=[]
        for i in range(n):
            x=0
            y=0
            for j in range(m):
                if grid[j][i]==0:
                    x+=1
                else:
                    y+=1
            b.append(y-x)
        for i in range(m):
            for j in range(n):
                grid[i][j]=a[i]+b[j]
        return grid