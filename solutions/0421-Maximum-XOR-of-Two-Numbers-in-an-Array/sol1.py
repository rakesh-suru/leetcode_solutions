class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                ans = max(ans, nums[i] ^ nums[j])
        
        return ans