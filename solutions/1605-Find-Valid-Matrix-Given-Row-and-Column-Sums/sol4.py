class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r, c = len(rowSum), len(colSum)
        ans = [[0] * c for _ in range(r)]
        i, j = 0, 0
        
        while i < r and j < c:
            ans[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= ans[i][j]
            colSum[j] -= ans[i][j]

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1
            
        return ans