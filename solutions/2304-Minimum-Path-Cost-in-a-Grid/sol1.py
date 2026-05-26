class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        def solve(row, col):

            if row == m - 1:
                return grid[row][col]

            ans = float('inf')

            current = grid[row][col]

            for next_col in range(n):

                move = moveCost[current][next_col]

                cost = (
                    grid[row][col] +
                    move +
                    solve(row + 1, next_col)
                )

                ans = min(ans, cost)

            return ans

        final_ans = float('inf')

        for col in range(n):
            final_ans = min(final_ans, solve(0, col))

        return final_ans