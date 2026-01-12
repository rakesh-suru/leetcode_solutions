class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = [int(char) for char in s]
        while len(nums) > 2:
            new_nums = []
            for i in range(len(nums) - 1):
                new_digit = (nums[i] + nums[i + 1]) % 10
                new_nums.append(new_digit)
            nums = new_nums
        return nums[0] == nums[1]