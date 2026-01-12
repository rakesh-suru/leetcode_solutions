class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxlen = 0
        current = 0
        
        for num in nums:
            if num == 1:
                current += 1
                maxlen = max(maxlen, current)
            else:
                current = 0
        
        return maxlen
