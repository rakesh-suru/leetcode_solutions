class Solution:
    def smallerNumbersThanCurrent(self, nums):
        temp = sorted(nums)
        mapping = {}
        for i, num in enumerate(temp):
            if num not in mapping:
                mapping[num] = i
        return [mapping[num] for num in nums]
