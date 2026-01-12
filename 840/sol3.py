class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(r, c):
            if grid[r+1][c+1] != 5:
                return False

            s = set()
            for i in range(3):
                for j in range(3):
                    s.add(grid[r+i][c+j])
            if s != {1,2,3,4,5,6,7,8,9}:
                return False

            return (
                grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15 and
                grid[r+1][c] + 5 + grid[r+1][c+2] == 15 and
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15 and
                grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 and
                grid[r][c+1] + 5 + grid[r+2][c+1] == 15 and
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15 and
                grid[r][c] + 5 + grid[r+2][c+2] == 15 and
                grid[r][c+2] + 5 + grid[r+2][c] == 15
            )

        ans = 0
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                if is_magic(r, c):
                    ans += 1
        return ans
