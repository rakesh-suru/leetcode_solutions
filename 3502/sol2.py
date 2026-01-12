class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = [cost[0]]
        for i in range(1, len(cost)):
            if cost[i] < ans[i-1]:
                ans.append(cost[i])
            else:
                ans.append(ans[i-1])
        return ans