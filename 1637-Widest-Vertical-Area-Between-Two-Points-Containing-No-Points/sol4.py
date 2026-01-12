class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = 0
        temp = []
        for i in points:
            temp.append(i[0])
        temp.sort()


        for i in range(len(temp)):
            if ans < temp[i] - temp[i-1]:
                ans = temp[i] - temp[i-1]
        
        return ans
