class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeros = 0
        maxlen = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            
            if zeros > k:
                if not nums[l]:
                    zeros -= 1
                l += 1
            
            maxlen = max(maxlen, r - l + 1)
        
        return maxlen
