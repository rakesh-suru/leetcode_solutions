class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        n = len(colors)

        for i in range(n):
            for j in range(i, n):
                if colors[i] != colors[j]:
                    ans = max(ans, j - i)
        
        return ans