class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        prev = matrix[0][:]

        for i in range(1, n):

            curr = [float("inf")] * n

            for j in range(n):

                for k in [-1, 0, 1]:

                    prev_col = j + k

                    if 0 <= prev_col < n:

                        curr[j] = min(
                            curr[j],
                            matrix[i][j] + prev[prev_col]
                        )

            prev = curr

        return min(prev)