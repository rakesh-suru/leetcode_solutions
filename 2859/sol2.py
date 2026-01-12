class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(nums[i] for i in range(len(nums)) if bin(i)[2:].count('1') == k)