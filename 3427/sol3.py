class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix = [0] + list(accumulate(nums))
        ans = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            ans += prefix[i + 1] - prefix[start]
        return ans
