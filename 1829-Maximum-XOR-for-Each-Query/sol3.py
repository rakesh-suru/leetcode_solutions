class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_xor = (1 << maximumBit) - 1
        ans = []
        for i in range(len(nums)-1, -1, -1):
            xor_sum = 0
            for j in range(i+1):
                xor_sum ^= nums[j]
            ans.append(xor_sum ^ max_xor)
        return ans
