class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = [int(c) for c in s]
        for x in range(len(nums) - 1, 1, -1):
            for i in range(x):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        return nums[0] == nums[1]
