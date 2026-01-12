from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    size = 1
                    valid = True
                    while i + size < m and j + size < n and valid:
                        for k in range(j, j + size + 1):
                            if matrix[i + size][k] == 0:
                                valid = False
                                break
                        for k in range(i, i + size + 1):
                            if matrix[k][j + size] == 0:
                                valid = False
                                break
                        if valid:
                            size += 1
                        else:
                            break
                    ans += size
        return ans
