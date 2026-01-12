class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digitSum = sum((map(int, ''.join(map(str,nums)))))
        return sum(nums) - digitSum