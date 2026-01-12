class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * (n + 1)
        right = [0] * (n + 1)

        for i in range(1, n + 1):
            if nums[i - 1] == 1:
                left[i] = left[i - 1] + 1
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                right[i] = right[i + 1] + 1

        ans = 0
        for i in range(n):
            ans = max(ans, left[i] + right[i + 1])

        return ans