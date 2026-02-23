class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                temp = sum(nums[i : j + 1])
                if temp == goal:
                    ans += 1
        return ans