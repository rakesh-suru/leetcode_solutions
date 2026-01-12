class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(r, c):
            s = set()
            for i in range(3):
                for j in range(3):
                    val = grid[r + i][c + j]
                    if val < 1 or val > 9 or val in s:
                        return False
                    s.add(val)

            if (grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15 or
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != 15 or
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15):
                return False

            if (grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15 or
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15 or
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15):
                return False

            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
                return False

            return True

        rows, cols = len(grid), len(grid[0])
        ans = 0

        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    ans += 1

        return ans
