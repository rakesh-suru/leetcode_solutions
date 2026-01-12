class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in nums:
            if i < k:
                ans += 1
        return sum(1 for i in nums if i < k)