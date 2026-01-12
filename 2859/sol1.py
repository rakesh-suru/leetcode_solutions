class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for index, num in enumerate(nums):
            if bin(index)[2:].count('1') == k:
                ans += num
        return ans