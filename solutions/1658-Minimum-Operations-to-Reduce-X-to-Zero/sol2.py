class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        ans = float("inf")

        @cache(None)
        def solve(arr, rem, steps):
            nonlocal ans

            if rem == 0:
                ans = min(ans, steps)
                return
            
            if rem < 0 or len(arr) == 0:
                return

            solve(arr[1:], rem - arr[0], steps + 1)
            solve(arr[:-1], rem - arr[-1], steps + 1)

        solve(nums, x, 0)

        return -1 if ans == float("inf") else ans