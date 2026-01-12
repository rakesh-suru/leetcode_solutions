class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        copy = [row[:] for row in matrix]

        for i in range(m):
            for j in range(n):
                if copy[i][j] == 0:
                    for k in range(n):
                        matrix[i][k] = 0
                    for k in range(m):
                        matrix[k][j] = 0
