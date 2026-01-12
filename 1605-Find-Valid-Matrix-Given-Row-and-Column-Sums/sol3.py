class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r, c = len(rowSum), len(colSum)
        ans = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if rowSum[i] == 0:
                    break
                x = min(rowSum[i], colSum[j])
                ans[i][j] = x
                rowSum[i] -= x
                colSum[j] -= x

        return ans
