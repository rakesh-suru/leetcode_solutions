class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        ans = 0
        heights = [0] * n

        for i in range(m):

            for j in range(n):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            sorted_heights = sorted(heights, reverse=True)

            for j in range(n):
                area = sorted_heights[j] * (j + 1)
                ans = max(ans, area)

        return ans