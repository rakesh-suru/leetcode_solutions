class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        ans = original
        for i in range(len(nums)):
            if ans in nums:
                ans *= 2
            else:
                break
        return ans
