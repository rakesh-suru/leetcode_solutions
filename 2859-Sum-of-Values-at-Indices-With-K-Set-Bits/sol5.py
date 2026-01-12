class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        if k == 0: return nums[0]
        d, res = [0] * len(nums), 0
        for i in range(1, len(nums)):
            d[i] = 1 + d[i & (i - 1)]
            if d[i] == k: res += nums[i]

        return res