class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + list(reversed(nums))