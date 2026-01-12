class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:       
        row = len(rowSum)
        col = len(colSum)
        ans = [[0] * col for _ in range(row)]

        for r in range(row):
            for c in range(col):
                temp = min(rowSum[r], colSum[c])
                ans[r][c] = temp
                rowSum[r] -= temp
                colSum[c] -= temp
        
        return ans