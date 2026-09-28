class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        prev_heights = [0] * n

        for i in range(m):
            heights = matrix[i][:]

            for j in range(n):
                if heights[j]:
                    heights[j] += prev_heights[j]
                
            sorted_heights = sorted(heights, reverse = True)

            for k in range(n):
                ans = max(ans, sorted_heights[k] * (k + 1))
            
            prev_heights = heights[:]
        
        return ans