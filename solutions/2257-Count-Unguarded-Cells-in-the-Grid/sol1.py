class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]

        for row, col in guards:
            matrix[row][col] = 1
        for row, col in walls:
            matrix[row][col] = 2
        
        def mark_guarded(row, col):
            for r in range(row+1, m):
                if matrix[r][col] in [1, 2]:
                    break
                matrix[r][col] = 3
            for r in reversed(range(0, row)):
                if matrix[r][col] in [1, 2]:
                    break
                matrix[r][col] = 3

            for c in range(col+1, n):
                if matrix[row][c] in [1, 2]:
                    break
                matrix[row][c] = 3
            for c in reversed(range(0, col)):
                if matrix[row][c] in [1, 2]:
                    break
                matrix[row][c] = 3

        for row, col in guards:
            mark_guarded(row, col)

        res = 0
        for row in matrix:
            for n in row:
                if n == 0:
                    res += 1
        return res
