class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - 2*k + 1):
            first = nums[i:i+k]
            second = nums[i+k:i+2*k]
            if first == sorted(first) and second == sorted(second) and \
               len(set(first)) == k and len(set(second)) == k:
                return True
        return False
