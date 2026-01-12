class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [val for i in range(0, len(nums), 2) for val in [nums[i+1]] * nums[i]]