class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag, max_area, idx = 0, 0, 0
        for i, (l, w) in enumerate(dimensions):
            diag = sqrt(l*l + w*w)
            area = l * w
            if diag > max_diag or (diag == max_diag and area > max_area):
                max_diag, max_area, idx = diag, area, i
        return dimensions[idx][0] * dimensions[idx][1]
