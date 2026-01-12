class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        index = 1
        length = len(nums)
        while index <= length:
            for i in range(nums[index-1]):
                ans.append(nums[index])
            index += 2
        
        return ans