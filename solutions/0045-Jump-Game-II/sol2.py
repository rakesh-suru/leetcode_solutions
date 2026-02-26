class Solution:
    def jump(self, nums: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def solve(idx):
            if idx >= len(nums) - 1:
                return 0

            if nums[idx] == 0:
                return float('inf')

            ans = float('inf')
            for step in range(1, nums[idx] + 1):
                ans = min(ans, 1 + solve(idx + step))

            return ans

        return solve(0)