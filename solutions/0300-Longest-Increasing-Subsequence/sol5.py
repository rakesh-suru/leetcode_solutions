class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        next_row = [0] * (n + 1)

        for idx in range(n - 1, -1, -1):
            curr = [0] * (n + 1)

            for prev in range(idx - 1, -2, -1):
                pick = 0

                if prev == -1 or nums[idx] > nums[prev]:
                    pick = 1 + next_row[idx + 1]

                not_pick = next_row[prev + 1]

                curr[prev + 1] = max(pick, not_pick)

            next_row = curr

        return next_row[0]