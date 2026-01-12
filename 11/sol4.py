class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                h = height[left]
                max_area = max(max_area, h * (right - left))
                while left < right and height[left] <= h:
                    left += 1
            else:
                h = height[right]
                max_area = max(max_area, h * (right - left))
                while left < right and height[right] <= h:
                    right -= 1
        return max_area
