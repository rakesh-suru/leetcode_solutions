class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        length = len(nums)
        res = 0
        for index, num in enumerate(nums):
            temp = nums[index:]
            m = max(temp)
            if res < m - num:
                res = m - num
        return res if res > 0 else -1