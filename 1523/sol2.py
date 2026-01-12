class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high+1):
            if i % 2 != 0:
                ans += 1
        return ans