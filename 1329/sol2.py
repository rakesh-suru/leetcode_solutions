class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        diag = defaultdict(list)

        for r in range(m):
            for c in range(n):
                diag[r-c].append(mat[r][c])

        for k in diag:
            diag[k].sort(reverse=True)

        for r in range(m):
            for c in range(n):
                mat[r][c] = diag[r-c].pop()

        return mat
