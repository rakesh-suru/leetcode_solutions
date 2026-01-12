class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        x = xor_sum ^ k
        count = 0
        while x:
            x &= x - 1
            count += 1
        return count
