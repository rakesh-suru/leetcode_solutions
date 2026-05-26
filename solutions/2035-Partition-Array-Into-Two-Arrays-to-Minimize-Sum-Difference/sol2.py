class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        half = n // 2
        total = sum(nums)

        memo = {}

        def solve(idx, count, curr_sum):

            if count > half:
                return float("inf")

            if idx == n:
                if count == half:
                    other = total - curr_sum
                    return abs(curr_sum - other)
                return float("inf")

            state = (idx, count, curr_sum)

            if state in memo:
                return memo[state]

            take = solve(
                idx + 1,
                count + 1,
                curr_sum + nums[idx]
            )

            not_take = solve(
                idx + 1,
                count,
                curr_sum
            )

            memo[state] = min(take, not_take)

            return memo[state]

        return solve(0, 0, 0)