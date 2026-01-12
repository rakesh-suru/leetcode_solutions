class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        arr = []
        for row in matrix:
            for val in row:
                arr.append(val)

        neg_cnt = sum(1 for x in arr if x < 0)
        total = sum(abs(x) for x in arr)

        if neg_cnt % 2 == 0:
            return total
        return total - 2 * min(abs(x) for x in arr)
