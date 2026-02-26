class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = float('inf')

        def solve(idx, jumps):
            nonlocal ans

            if jumps >= ans:
                return

            if idx >= len(nums) - 1:
                ans = min(ans, jumps)
                return

            for step in range(1, nums[idx] + 1):
                solve(idx + step, jumps + 1)

        solve(0, 0)
        return ans