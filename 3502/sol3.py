class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans=[]
        lowest=float("inf")
        for i in range(len(cost)):
            if lowest > cost[i]:
                lowest = cost[i]
            ans.append(lowest)
        return ans