class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        neg_cnt = 0
        mini = float('inf')
        total = 0
        for i in range(n):
            for j in range(n):
                total += abs(matrix[i][j])
                mini = min(mini, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    neg_cnt += 1
                
        if neg_cnt % 2 == 0:
            return total
        else:
            return total - mini * 2