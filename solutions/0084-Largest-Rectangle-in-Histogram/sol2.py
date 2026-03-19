class Solution:
    
    def pse(self, heights):
        stack = []
        pse = [-1] * len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                pse[i] = stack[-1]
            
            stack.append(i)
        
        return pse

    def nse(self, heights):
        stack = []
        n = len(heights)
        nse = [n] * n

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                nse[i] = stack[-1]
            
            stack.append(i)
        
        return nse

    def largestRectangleArea(self, heights: List[int]) -> int:
        pse = self.pse(heights)
        nse = self.nse(heights)

        max_area = 0

        for i in range(len(heights)):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        
        return max_area