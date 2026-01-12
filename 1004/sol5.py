class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            k -= nums[r] == 0
            if k < 0:
                k += nums[l] == 0
                l += 1
        return len(nums) - l
