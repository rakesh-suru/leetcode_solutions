class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        ans = 0

        for i in range(l):
            ans += mat[i][i]

        for i in range(l):
            if i != l - 1 - i:
                ans += mat[i][l - 1 - i]
        
        return ans
