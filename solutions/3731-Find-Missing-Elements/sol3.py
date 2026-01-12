class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        ans = []
        mini = min(nums)
        maxi = max(nums)

        for x in range(mini + 1, maxi):
            if x not in s:
                ans.append(x)

        return ans
