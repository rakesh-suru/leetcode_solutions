class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        zeros = 0
        maxlen = 0
    
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
        
            while zeros > 0:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
        
            maxlen = max(maxlen, r - l + 1)
        return maxlen