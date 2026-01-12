from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        ans = []
        row = col = 0
        up = True

        for _ in range(m * n):
            ans.append(mat[row][col])

            if up:
                if col == n - 1:
                    row += 1
                    up = False
                elif row == 0:
                    col += 1
                    up = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                    up = True
                elif col == 0:
                    row += 1
                    up = True
                else:
                    row += 1
                    col -= 1
        return ans
