class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp += nums[j]

                if temp == k:
                    ans += 1
        return ans