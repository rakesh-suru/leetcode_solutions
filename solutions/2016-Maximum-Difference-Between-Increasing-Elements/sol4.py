class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        min_num = nums[0]

        for i in range(len(nums)):
            max_diff = max(max_diff, nums[i] - min_num)
            min_num = min(min_num, nums[i])

        return max_diff if max_diff != 0 else -1

        