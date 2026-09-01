class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        total = sum(stones)
        ans = total
        prefix = total

        for i in range(n - 1, 1, -1):
            prefix -= stones[i]
            ans = max(ans, prefix - ans)

        return ans