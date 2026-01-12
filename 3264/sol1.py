class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            temp = min(nums)
            idx = nums.index(temp)
            nums[idx] = nums[idx] * multiplier
        return nums