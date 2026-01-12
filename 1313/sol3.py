class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        index = 1
        length = len(nums)
        while index <= length:
            ans.extend([nums[index]] * nums[index-1])
            index += 2
        return ans