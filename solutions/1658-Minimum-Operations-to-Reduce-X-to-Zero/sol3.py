class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        memo = {}

        def solve(left, right, rem):
            if rem == 0:
                return 0

            if rem < 0 or left > right:
                return float("inf")

            state = (left, right, rem)

            if state in memo:
                return memo[state]

            take_left = solve(
                left + 1,
                right,
                rem - nums[left]
            )

            take_right = solve(
                left,
                right - 1,
                rem - nums[right]
            )

            memo[state] = 1 + min(take_left, take_right)

            return memo[state]

        ans = solve(0, n - 1, x)

        return -1 if ans == float("inf") else ans