class Solution:
    def trap(self, height):
        n = len(height)
        maxes = [0] * n

        maxes[0] = height[0]
        for i in range(1, n):
            maxes[i] = max(maxes[i - 1], height[i])

        right_max = height[n - 1]
        total = 0

        for i in range(n - 1, -1, -1):
            right_max = max(right_max, height[i])
            total += min(maxes[i], right_max) - height[i]

        return total