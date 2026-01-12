class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def pascal(r, c):
            if c == 0 or c == r:
                return 1
            return pascal(r-1, c-1) + pascal(r-1, c)
    
        triangle = []
        for i in range(numRows):
            row = [pascal(i, j) for j in range(i + 1)]
            triangle.append(row)
        return triangle