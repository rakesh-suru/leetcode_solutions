class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 1):
            curr = nums[i]
            nextt = nums[i + 1]
            for x in range(curr + 1, nextt):
                ans.append(x)

        return ans
