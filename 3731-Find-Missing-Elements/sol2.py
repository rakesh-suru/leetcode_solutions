class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        mini = min(nums)
        maxi = max(nums)

        while mini < maxi:
            mini += 1
            if mini not in nums:
                ans.append(mini)
        return ans