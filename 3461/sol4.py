class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = [int(c) for c in s]
        
        def reduce(nums):
            if len(nums) == 2:
                return nums[0] == nums[1]
            new_nums = [(nums[i] + nums[i+1]) % 10 for i in range(len(nums)-1)]
            return reduce(new_nums)
        
        return reduce(nums)
