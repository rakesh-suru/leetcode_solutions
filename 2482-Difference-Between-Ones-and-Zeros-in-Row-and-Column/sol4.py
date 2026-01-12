import numpy as np

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        A = np.array(grid)
        row_ones = A.sum(axis=1).reshape(-1, 1)
        col_ones = A.sum(axis=0).reshape(1, -1)
        m, n = A.shape
        return (2 * (row_ones + col_ones) - (m + n)).tolist()
