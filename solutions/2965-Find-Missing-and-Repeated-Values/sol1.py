class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = [0] * (n * n + 1)

        for i in grid:
            for j in i:
                freq[j] += 1
        
        a = b = -1
        for num in range(1, n * n + 1):
            if freq[num] == 2:
                a = num
            if freq[num] == 0:
                b = num
        
        return [a,b]