class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        length = len(nums)
        res = 0
        for index, num in enumerate(nums):
            temp = nums[index:]
            for n in temp:
                if res < n - num:
                    res = n - num
        return res if res > 0 else -1