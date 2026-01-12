class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = [int(c) for c in s]
        n = len(nums)
        a = sum(comb(n-2, k) * nums[k] for k in range(n-1)) % 10
        b = sum(comb(n-2, k) * nums[k+1] for k in range(n-1)) % 10
        return a == b
