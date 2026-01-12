class Solution:
    def triangleType(self, nums: List[int]) -> str:
        size = 3
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        for i in range(len(nums)):
            if sum(nums[:i] + nums[i+1:]) <= nums[i]:
                return "none"
        for num in nums:
            if nums.count(num) == 2:
                return "isosceles"
        return "scalene"