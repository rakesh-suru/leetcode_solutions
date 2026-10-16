class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        temp = []

        for l, w in rectangles:
            temp.append(min(l, w))
        
        maxi = max(temp)
        ans = temp.count(maxi)
        
        return anss