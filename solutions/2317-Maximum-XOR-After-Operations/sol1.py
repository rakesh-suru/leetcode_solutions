class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        ans = 0

        for num in nums:
            ans = ans | num
        
        return ans