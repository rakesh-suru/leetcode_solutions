class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for m in grid:
            for n in m:
                if n < 0:
                    ans += 1
        return ans