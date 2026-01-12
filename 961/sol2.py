class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        num_set = set(nums)
        for num in num_set:
            if nums.count(num) == n:
                return num