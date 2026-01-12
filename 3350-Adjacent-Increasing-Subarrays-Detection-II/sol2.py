class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        def is_increasing(start, end):
            for i in range(start + 1, end):
                if nums[i] <= nums[i - 1]:
                    return False
            return True

        for k in range(1, n // 2 + 1):
            for i in range(n - 2 * k + 1):
                if is_increasing(i, i + k) and is_increasing(i + k, i + 2 * k):
                    res = k
        return res
