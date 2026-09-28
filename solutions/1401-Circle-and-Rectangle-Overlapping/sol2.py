class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        closeX = max(x1, min(xCenter, x2))
        closeY = max(y1, min(yCenter, y2))

        distance_sq = (closeX - xCenter) ** 2 + (closeY - yCenter) ** 2

        return distance_sq <= radius ** 2