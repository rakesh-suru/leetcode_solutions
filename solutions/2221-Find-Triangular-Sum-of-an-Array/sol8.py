class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        coeff = 1
        ans = 0
        for i in range(n):
            ans += coeff * nums[i]
            ans %= 10
            coeff = coeff * (n - 1 - i) // (i + 1) if i < n-1 else 1
        return ans % 10
