class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        sum_nums = sum(nums)
        while sum_nums % k != 0:
            res += 1
            sum_nums -= 1
        return res