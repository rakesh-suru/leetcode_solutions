class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def solve(i, j1, j2):
            if j1 < 0 or j1 >= n or j2 < 0 or j2 >= n:
                return -float("inf")
            
            if i == m-1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            
            temp = [-1, 0, 1]
            maxi = 0
            for d1 in temp:
                for d2 in temp:
                    if j1 == j2:
                        maxi = max(maxi, grid[i][j1] + solve(i + 1, j1 + d1, j2 + d2))
                    else:
                        maxi = max(maxi, grid[i][j1] + grid[i][j2] + solve(i + 1, j1 +d1, j2 + d2))
            return maxi

        return solve(0, 0, n - 1)
        