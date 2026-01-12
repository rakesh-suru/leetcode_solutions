class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = 0
        temp = []
        for i in points:
            temp.append(i[0])
        temp.sort()


        for i in range(len(temp)-1):
            if ans < temp[i+1] - temp[i]:
                ans = temp[i+1] - temp[i]
        
        return ans
