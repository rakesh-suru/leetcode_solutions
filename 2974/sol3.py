class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        i ,j = 0, 1
        while j < len(nums):
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j += 2
        return nums
