class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])

        def bubble_sort_diag(r, c):
            changed = True
            while changed:
                changed = False
                i, j = r, c

                while i + 1 < m and j + 1 < n:
                    if mat[i][j] > mat[i+1][j+1]:
                        mat[i][j], mat[i+1][j+1] = mat[i+1][j+1], mat[i][j]
                        changed = True
                    i += 1
                    j += 1

        for col in range(n):
            bubble_sort_diag(0, col)

        for row in range(1, m):
            bubble_sort_diag(row, 0)

        return mat
