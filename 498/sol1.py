class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 0 or len(mat[0]) == 0:
            return []
        ans = []
        m = len(mat)
        n = len(mat[0])
        up = True
        row = col = 0

        while row < m and col < n:
            if up:
                while row > 0 and col < n - 1:
                    ans.append(mat[row][col])
                    row -= 1
                    col += 1
                ans.append(mat[row][col])

                if col == n - 1:
                    row += 1
                else:
                    col += 1
            else:
                while row < m - 1 and col > 0:
                    ans.append(mat[row][col])
                    row += 1
                    col -= 1
                ans.append(mat[row][col])

                if row == m - 1:
                    col += 1
                else:
                    row += 1
            up = not up
        return ans
