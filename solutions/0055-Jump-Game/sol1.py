class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        for i, val in enumerate(nums):
            if i > max_idx:
                return False
            max_idx = max(max_idx, i + val)
        
        return True