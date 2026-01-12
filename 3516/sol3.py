class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a = (abs(x-z), 1)
        b = (abs(y-z), 2)
        if a[0] == b[0]:
            return 0
        return min(a, b)[1]
