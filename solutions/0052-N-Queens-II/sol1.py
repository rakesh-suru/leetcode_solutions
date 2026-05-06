class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag1 = set()
        diag2 = set()

        ans = 0
        board = [["."] * n for _ in range(n)]

        def solve(row):
            nonlocal ans
            if row == n:
                ans += 1
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = "Q"

                solve(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                board[row][col] = "."

        solve(0)
        return ans
