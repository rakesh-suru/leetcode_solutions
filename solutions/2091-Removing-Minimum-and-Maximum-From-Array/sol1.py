class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini = nums[0]
        maxi = nums[0]
        min_idx = 0
        max_idx = 0

        for i, num in enumerate(nums):
            if num > maxi:
                maxi = num
                max_idx = i
            
            if num < mini:
                mini = num
                min_idx = i
        
        n = len(nums)
        mid = n//2

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        return min(
            right + 1,
            n - left,
            (left + 1) + (n - right)
        )