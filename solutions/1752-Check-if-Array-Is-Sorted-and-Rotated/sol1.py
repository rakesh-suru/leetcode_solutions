class Solution:
    def check(self, nums: List[int]) -> bool:
        temp = sorted(nums)

        for i in range(len(nums)):
            if nums[i:] + nums[:i] == temp:
                return True
        return False