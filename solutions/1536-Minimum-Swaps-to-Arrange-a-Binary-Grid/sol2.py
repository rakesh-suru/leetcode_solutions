class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        last = []
        for row in grid:
            idx = -1
            for j in range(n):
                if row[j] == 1:
                    idx = j
            last.append(idx)
        
        swaps = 0

        for i in range(n):
            j = i

            while j < n and last[j] > i:
                j += 1
            
            if j == n:
                return -1

            while j > i:
                last[j], last[j - 1] = last[j - 1], last[j]
                swaps += 1
                j -= 1
        
        return swaps