class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check_magic(mat):
            rows = len(mat)
            cols = len(mat[0])

            sum_arr = []
            for i in range(rows):
                for j in range(cols):
                    if mat[i][j] > 9 or mat[i][j]<1:
                        return 0
                    if mat[i][j] not in sum_arr:
                        sum_arr.append(mat[i][j])
            
            rcnt = 0
            ccnt = 0
            dcnt = 0
            for i in range(rows):
                if sum(mat[i][:]) == 15:
                    rcnt += 1
            for j in range(cols):
                if sum(mat[i][j] for i in range(rows)) == 15:
                    ccnt += 1
            if mat[0][0] + mat[1][1] + mat[2][2] == 15:
                dcnt += 1
            if mat[0][2] + mat[1][1] + mat[2][0] == 15:
                dcnt += 1
                        
            if rcnt == 3 and ccnt == 3 and dcnt == 2 and sum(sum_arr) == 45:
                return 1
            
            
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows - 2):
            for c in range(cols - 2):
                if check_magic([sub[c:c+3] for sub in grid[r:r+3]]):
                    ans += 1
        return ans
