class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        def check(row, col):
            temp = 0
            
            if mat[row].count(1) == 1:
                temp += 1
                
            if sum(mat[i][col] for i in range(len(mat))) == 1:
                temp += 1
                
            return temp == 2

        ans = 0
        for i in range(len(mat)):
             for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if check(i, j):
                        ans += 1
        
        return ans