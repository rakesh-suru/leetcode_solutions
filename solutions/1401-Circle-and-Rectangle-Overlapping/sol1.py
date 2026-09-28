class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        closeX = float("inf")
        closeY = float("inf")

        if xCenter < x1:
            closeX = x1
        elif xCenter > x2:
            closeX = x2
        else:
            closeX = xCenter
        

        if yCenter < y1:
            closeY = y1
        elif yCenter > y2:
            closeY = y2
        else:
            closeY = yCenter
        

        distance_sq = (closeX - xCenter)**2 + (closeY - yCenter)**2

        if distance_sq <= radius ** 2:
            return True
        
        return False