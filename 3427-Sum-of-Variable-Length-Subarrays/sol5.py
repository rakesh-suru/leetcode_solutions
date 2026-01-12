class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            ans += prefix[i + 1] - prefix[start]
        return ans
