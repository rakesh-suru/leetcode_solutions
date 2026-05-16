class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] == nums[i + 1]:
                return False
        
        return nums.count(max(nums)) == 2 and len(nums) == max(nums) + 1