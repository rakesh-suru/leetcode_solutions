class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        temp = []

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    temp.append([row, col])

        for row, col in temp:
            for j in range(n):
                matrix[row][j] = 0
            for i in range(m):
                matrix[i][col] = 0
