class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] == 2 * nums[j] and nums[k] == 2 * nums[j]:
                        ans += 1
        return ans