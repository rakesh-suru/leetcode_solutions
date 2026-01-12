class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return sum(nums) - sum(int(d) for n in nums for d in str(n))