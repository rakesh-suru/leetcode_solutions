class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxi = max(nums)

        if len(nums) != maxi + 1:
            return False

        if nums.count(maxi) != 2:
            return False

        for i in range(1, maxi):
            if nums.count(i) != 1:
                return False

        return True