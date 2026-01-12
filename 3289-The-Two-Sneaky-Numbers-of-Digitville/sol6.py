class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] and (not res or res[-1] != nums[i]):
                res.append(nums[i])
        return res
