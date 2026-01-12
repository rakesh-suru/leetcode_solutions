class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        for i in range(nums[0], nums[-1]+1):
            if i not in nums:
                ans.append(i)
        return ans