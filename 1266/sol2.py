class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)-1):
            t1 = abs(points[i][0] - points[i+1][0])
            t2 = abs(points[i][1] - points[i+1][1])
            temp = max(t1, t2)
            ans += temp
        
        return ans