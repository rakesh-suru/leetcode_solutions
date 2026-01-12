class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(0) == 0:
            return len(nums)-1
        keep = delete = 0
        ans = 0

        for num in nums:
            if num == 1:
                keep += 1
                delete += 1
            else:
                delete = keep
                keep = 0
            ans = max(ans, delete)

        return ans
