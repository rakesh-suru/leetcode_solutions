class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum_nums = sum(nums)
        return sum_nums % k