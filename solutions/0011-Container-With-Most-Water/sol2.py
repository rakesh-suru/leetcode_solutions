class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        for i in range(n-1):
            for j in range(i+1, n):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))
        return max_area
