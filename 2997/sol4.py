class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(1 for bit in bin(reduce(xor, nums) ^ k) if bit == '1')
