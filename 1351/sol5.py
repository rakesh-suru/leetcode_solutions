class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(map(lambda row: sum(1 for num in row if num < 0), grid))
