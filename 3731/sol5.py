class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)

        nums = set(nums)
        temp = set([i for i in range(mini, maxi+1)])
        return sorted(list(temp - nums))