class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        ans = 0

        for i, c in enumerate(cost):
            if i % 3 != 2:
                ans += c

        return ans