class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even = 0
        for n in nums:
            if n % 2 == 0:
                even += 1
        return ([0] * even) + ([1] * (len(nums) - even))