class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        for i in range(m):
            grid[i].sort()

        for j in range(n):
            maxi = 0

            for i in range(m):
                maxi = max(maxi, grid[i][j])

            ans += maxi

        return ans