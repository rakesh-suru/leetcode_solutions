class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort(key = lambda x:x[0])


        for i in range(len(points)-1):
            if ans < points[i+1][0] - points[i][0]:
                ans = points[i+1][0] - points[i][0]
        
        return ans
