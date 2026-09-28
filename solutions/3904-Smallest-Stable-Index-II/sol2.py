class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_prefix = [0] * n
        min_prefix[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            min_prefix[i] = min(min_prefix[i + 1], nums[i])
        
        max_num = nums[0]
        for i in range(n):
            max_num = max(max_num, nums[i])
            if max_num - min_prefix[i] <= k:
                return i
        
        return -1