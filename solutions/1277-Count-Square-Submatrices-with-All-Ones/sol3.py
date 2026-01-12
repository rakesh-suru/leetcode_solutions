from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        prev = [0] * n
        ans = 0

        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        curr[j] = 1
                    else:
                        curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
                    ans += curr[j]
            prev = curr
        return ans
