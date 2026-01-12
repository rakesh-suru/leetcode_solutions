class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d = {1: abs(x-z), 2: abs(y-z)}
        min_dist = min(d.values())
        if list(d.values()).count(min_dist) > 1:
            return 0
        return min(d, key=d.get)
