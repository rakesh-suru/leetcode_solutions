class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        pts = sorted(points, key=lambda p: (p[0], -p[1]))
        n = len(pts)
        ans = 0

        for i in range(n):
            x1, y1 = pts[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = pts[j]

                if not (x1 <= x2 and y1 >= y2 and (x1 < x2 or y1 > y2)):
                    continue

                ok = True
                for k in range(n):
                    if k == i or k == j:
                        continue
                    x, y = pts[k]
                    if x1 <= x <= x2 and y2 <= y <= y1:
                        ok = False
                        break
                if ok:
                    ans += 1
        return ans
