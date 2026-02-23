class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        temp = (xor ^ (xor - 1)) & xor

        b1 = 0
        b2 = 0

        for num in nums:
            if num & temp == 0:
                b1 ^= num
            else:
                b2 ^= num
        
        return [b1, b2]