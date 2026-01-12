class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i:])
            if abs(left_sum - right_sum) % 2 == 0:
                ans += 1
        return ans