class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i,j = 0,1
        ans = []
        while j <= len(nums):
            for num in range(nums[i]):
                ans.append(nums[j])
            i += 2
            j += 2
        
        return ans