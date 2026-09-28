class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        visited = [[False] * n for _ in range(m)]

        for _ in range(n):
            to_del = -1

            for i in range(m):
                maxi = -1
                pos = -1

                for j in range(n):
                    if not visited[i][j] and grid[i][j] > maxi:
                        maxi = grid[i][j]
                        pos = j

                visited[i][pos] = True
                to_del = max(to_del, maxi)

            ans += to_del

        return ans