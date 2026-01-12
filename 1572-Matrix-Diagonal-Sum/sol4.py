class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        return sum(
            mat[i][i] + (mat[i][n-1-i] if i != n-1-i else 0)
            for i in range(n)
        )
