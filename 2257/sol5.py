class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]

        for (row, col) in guards:
            matrix[row][col] = 1
        for (row, col) in walls:
            matrix[row][col] = 2

        for row in range(m):
            guard = False
            for col in range(n):
                if matrix[row][col] == 1:
                    guard = True
                elif matrix[row][col] == 2:
                    guard = False
                if not matrix[row][col] and guard:
                    matrix[row][col] = 3
            guard = False
            for col in reversed(range(n)):
                if matrix[row][col] == 1:
                    guard = True
                elif matrix[row][col] == 2:
                    guard = False
                if not matrix[row][col] and guard:
                    matrix[row][col] = 3
        
        for col in range(n):
            guard = False
            for row in range(m):
                if matrix[row][col] == 1:
                    guard = True
                elif matrix[row][col] == 2:
                    guard = False
                if not matrix[row][col] and guard:
                    matrix[row][col] = 3
            guard = False
            for row in reversed(range(m)):
                if matrix[row][col] == 1:
                    guard = True
                elif matrix[row][col] == 2:
                    guard = False
                if not matrix[row][col] and guard:
                    matrix[row][col] = 3

        ans = 0
        for row in matrix:
            for n in row:
                if n == 0:
                    ans += 1
        return ans