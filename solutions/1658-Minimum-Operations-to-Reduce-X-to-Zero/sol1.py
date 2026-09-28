class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        ans = float("inf")

        def solve(left, right, rem, steps):
            nonlocal ans

            if rem < 0:
                return

            if rem == 0:
                ans = min(ans, steps)
                return

            if left > right:
                return

            solve(left + 1, right, rem - nums[left], steps + 1)

            solve(left, right - 1, rem - nums[right], steps + 1)

        solve(0, n - 1, x, 0)

        return -1 if ans == float("inf") else ans