class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total = n * n * (n * n + 1)//2

        seen = set()
        actual = 0
        repeat = -1

        for row in grid:
            for val in row:
                if val in seen:
                    repeat = val
                seen.add(val)
                actual += val
        
        missing = total - (actual - repeat)
        return[repeat, missing]