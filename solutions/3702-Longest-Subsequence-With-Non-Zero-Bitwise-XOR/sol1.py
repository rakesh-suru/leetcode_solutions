class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        nonzero = False

        for num in nums:
            xor ^= num

            if num != 0:
                nonzero = True

        if xor != 0:
            return n

        if nonzero:
            return n - 1

        return 0