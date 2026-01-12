class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainder_count = Counter(num % value for num in nums)
        mex = 0
        while True:
            r = mex % value
            if remainder_count[r] > 0:
                remainder_count[r] -= 1
                mex += 1
            else:
                return mex
