class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ans = float("inf")
        for i in range(len(nums)):
            curr = str(nums[i])[::-1]
            for j in range(i + 1, len(nums)):
                if int(curr) == nums[j]:
                    ans = min(ans, abs(j - i))
        return -1 if ans == float("inf") else ans