class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r = 0
        c = 0
        l = len(mat)
        ans = 0
        while r < l:
            ans += mat[r][c]
            r += 1
            c += 1
        
        r = 0
        c = l-1
        while r < l:
            ans += mat[r][c]
            r += 1
            c -= 1
        
        if l % 2 == 1:
            double = mat[l//2][l//2]
            return ans - double
        return ans