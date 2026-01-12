class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = len(nums)
        for i in nums:
            if i >= k:
                ans -= 1
        return ans