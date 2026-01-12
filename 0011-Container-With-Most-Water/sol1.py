class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n  = len(height)
        for i in range(n-1):
            for j in range(i+1, n):
                left = height[i]
                right = height[j]
                dist = j - i
                max_area = max(max_area, min(left, right) * dist)
        return max_area