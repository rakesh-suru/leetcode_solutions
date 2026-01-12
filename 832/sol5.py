class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[x ^ 1 for x in row[::-1]] for row in image]
