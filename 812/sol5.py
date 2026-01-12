class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
        
        def area(p1, p2, p3):
            return abs(
                p1[0]*(p2[1]-p3[1]) +
                p2[0]*(p3[1]-p1[1]) +
                p3[0]*(p1[1]-p2[1])
            ) / 2

        points = sorted(points)
        hull = []
        for p in points:
            while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        t = len(hull) + 1
        for p in reversed(points[:-1]):
            while len(hull) >= t and cross(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        hull.pop()

        n = len(hull)
        max_area = 0

        for i in range(n):
            k = (i + 2) % n
            for j in range(i+1, n):
                while True:
                    cur = area(hull[i], hull[j], hull[k])
                    nxt = area(hull[i], hull[j], hull[(k+1)%n])
                    if nxt > cur:
                        k = (k+1) % n
                    else:
                        break
                max_area = max(max_area, area(hull[i], hull[j], hull[k]))
        return max_area
