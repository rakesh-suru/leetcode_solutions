class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zeros = 0
        ans = 0

        for r, val in enumerate(nums):
            if val == 0:
                zeros += 1

            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            ans = max(ans, r - l)
        return ans