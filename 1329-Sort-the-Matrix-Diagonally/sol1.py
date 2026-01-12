class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        def sorting(mat, row, col, m, n):
            r = row
            c = col
            temp = []
            while(r < m and c < n):
                temp.append(mat[r][c])
                r += 1
                c += 1
            
            temp.sort()

            r = row
            c = col
            i = 0
            while(r < m and c < n):
                mat[r][c] = temp[i]
                r += 1
                c += 1
                i += 1

        m = len(mat)
        n = len(mat[0])

        for col in range(n):
            sorting(mat, 0, col, m, n)
        
        for row in range(m):
            sorting(mat, row, 0, m, n)
        
        return mata
