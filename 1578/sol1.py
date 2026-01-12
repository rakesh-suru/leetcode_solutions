class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        left = 0
        for right in range(1, len(colors)):
            if colors[left] == colors[right]:
                if neededTime[left] > neededTime[right]:
                    ans += neededTime[right]
                else:
                    ans += neededTime[left]
                    left = right
            else:
                left = right
        return ans