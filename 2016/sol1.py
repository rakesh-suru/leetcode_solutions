class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        length = len(nums)
        res = 0
        for i in range(length):
            for j in range(i+1, length):
                if nums[j] > nums[i] and res < nums[j] - nums[i]:
                    res = nums[j] - nums[i]
        if res > 0:
            return res
        return -1