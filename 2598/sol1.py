from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainder_count = Counter()

        for num in nums:
            remainder = num % value
            remainder_count[remainder] += 1

        mex = 0
        while True:
            remainder = mex % value
            if remainder_count[remainder] > 0:
                remainder_count[remainder] -= 1
                mex += 1
            else:
                return mex
