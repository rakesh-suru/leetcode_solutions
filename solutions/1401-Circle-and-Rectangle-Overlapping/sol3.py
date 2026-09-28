class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        if xCenter < x1:
            dx = x1 - xCenter
        elif xCenter > x2:
            dx = xCenter - x2
        else:
            dx = 0

        if yCenter < y1:
            dy = y1 - yCenter
        elif yCenter > y2:
            dy = yCenter - y2
        else:
            dy = 0

        return dx * dx + dy * dy <= radius * radius