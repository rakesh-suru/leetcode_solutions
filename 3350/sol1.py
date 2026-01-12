class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for k in range(1, n // 2 + 1):
            for i in range(n - 2 * k + 1):
                a, b = nums[i:i+k], nums[i+k:i+2*k]
                if a == sorted(a) and b == sorted(b) and len(set(a)) == k and len(set(b)) == k:
                    res = k
        return res
