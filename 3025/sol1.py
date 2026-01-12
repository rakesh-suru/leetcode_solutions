class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0

        for i in range(n):
            for j in range(n):
                if i == j: 
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 <= x2 and y1 >= y2 and (x1 < x2 or y1 > y2):
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x, y = points[k]
                        if x1 <= x <= x2 and y2 <= y <= y1:
                            valid = False
                            break
                    if valid:
                        ans += 1
        return ans