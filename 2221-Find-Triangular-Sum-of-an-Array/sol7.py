class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            ans += math.comb(n-1, i) * nums[i]
        return ans % 10
