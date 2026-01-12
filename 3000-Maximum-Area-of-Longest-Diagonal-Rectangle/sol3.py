class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dimensions.sort(key=lambda x: (x[0]**2 + x[1]**2, x[0]*x[1]))
        l, w = dimensions[-1]
        return l * w
