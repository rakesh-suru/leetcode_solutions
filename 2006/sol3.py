class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            target = nums[i] + k
            left = bisect.bisect_left(nums, target, i + 1)
            right = bisect.bisect_right(nums, target, i + 1)
            ans += right - left
        return ans
