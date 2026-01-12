class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_cnt = 0
        mini = float('inf')
        total = 0
        for row in matrix:
            for num in row:
                total += abs(num)
                mini = min(mini, abs(num))
                if num < 0:
                    neg_cnt += 1
                
        if neg_cnt & 1:
            return total - mini * 2
        return total