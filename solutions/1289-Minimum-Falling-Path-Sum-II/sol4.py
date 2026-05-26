class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        prev = grid[0][:]

        for row in range(1, n):

            curr = [0] * n

            min1 = float("inf")
            min2 = float("inf")

            min1_col = -1

            for col in range(n):

                val = prev[col]

                if val < min1:
                    min2 = min1
                    min1 = val
                    min1_col = col

                elif val < min2:
                    min2 = val

            for col in range(n):

                if col != min1_col:
                    curr[col] = grid[row][col] + min1
                else:
                    curr[col] = grid[row][col] + min2

            prev = curr

        return min(prev)