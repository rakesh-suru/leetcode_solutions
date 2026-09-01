class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            if k * (i + 1) not in nums:
                return k * (i + 1)
        
        return k * (n + 1)