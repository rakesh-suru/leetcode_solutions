class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        if xor != 0:
            return len(nums)

        if any(nums):
            return len(nums) - 1

        return 0