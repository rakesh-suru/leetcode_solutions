class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_xor = (1 << maximumBit) - 1
        n = len(nums)
        prefix_xor = [0] * n
        prefix_xor[0] = nums[0]
        for i in range(1, n):
            prefix_xor[i] = prefix_xor[i-1] ^ nums[i]
        
        ans = []
        for i in range(n-1, -1, -1):
            ans.append(prefix_xor[i] ^ max_xor)
        return ans
