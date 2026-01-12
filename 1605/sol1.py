class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r = len(rowSum)
        c = len(colSum)

        ans = [[0] * c for _ in range(r)]

        for row in range(r):
            ans[row][0] = rowSum[row]
        
        for col in range(c):
            temp = 0
            for row in range(r):
                temp += ans[row][col]
            
            row = 0
            while temp > colSum[col]:
                diff = temp - colSum[col]
                shift = min(ans[row][col], diff)

                ans[row][col] -= shift
                ans[row][col+1] += shift
                temp -= shift
                row += 1
        
        return ans
