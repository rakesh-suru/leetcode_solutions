class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)-1):
            p1 = points[i]
            p2 = points[i+1]
            t1 = abs(p1[0] - p2[0])
            t2 = abs(p1[1] - p2[1])
            temp = max(t1, t2)
            ans += temp
        
        return ans