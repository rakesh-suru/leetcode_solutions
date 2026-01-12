class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        for index, num in enumerate(nums):
            if num == target:
                ans.append(index)
        return ans
        