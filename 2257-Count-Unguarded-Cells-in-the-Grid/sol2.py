class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]

        for r, c in guards:
            matrix[r][c] = 1
        for r, c in walls:
            matrix[r][c] = 2

        def is_guarded(x, y):

            for i in range(x - 1, -1, -1):
                if matrix[i][y] == 2: break
                if matrix[i][y] == 1: return True

            for i in range(x + 1, m):
                if matrix[i][y] == 2: break
                if matrix[i][y] == 1: return True

            for j in range(y - 1, -1, -1):
                if matrix[x][j] == 2: break
                if matrix[x][j] == 1: return True

            for j in range(y + 1, n):
                if matrix[x][j] == 2: break
                if matrix[x][j] == 1: return True
            return False

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and not is_guarded(i, j):
                    res += 1

        return res
