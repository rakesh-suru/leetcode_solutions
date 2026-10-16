class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxi = 0
        ans = 0

        for l, w in rectangles:
            temp = min(l, w)
            if temp > maxi:
                maxi = temp
                ans = 1
            elif temp == maxi:
                ans += 1
        
        return ans