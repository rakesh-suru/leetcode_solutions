class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        prev = grid[n - 1][:]

        for row in range(n - 2, -1, -1):

            curr = [0] * n

            for col in range(n):

                temp = float("inf")

                for next_col in range(n):

                    if next_col != col:
                        temp = min(temp, prev[next_col])

                curr[col] = grid[row][col] + temp

            prev = curr

        return min(prev)