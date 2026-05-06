class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        for i in range(n):
            for j in range(n):
                if nums[i] == nums[j]:
                    ans[i] += abs(j - i)
        return ans