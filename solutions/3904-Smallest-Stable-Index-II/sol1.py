class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        max_prefix = [0] * n
        max_prefix[0] = nums[0]
        min_prefix = [0] * n
        min_prefix[-1] = nums[-1]

        for i in range(1, n):
            max_prefix[i] = max(max_prefix[i - 1], nums[i])
        
        for i in range(n - 2, -1, -1):
            min_prefix[i] = min(min_prefix[i + 1], nums[i])
        
        for i in range(n):
            if max_prefix[i] - min_prefix[i] <= k:
                return i
        
        return -1