class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        row = []
        for i in range(numRows):
            row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1] if row else [1]
            triangle.append(row)
        return triangle