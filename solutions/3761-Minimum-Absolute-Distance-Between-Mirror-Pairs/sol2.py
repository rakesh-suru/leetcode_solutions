class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        pos = {}
        ans = float("inf")

        for i, num in enumerate(nums):
            rev = int(str(num)[::-1])

            if rev in pos:
                ans = min(ans, i - pos[rev])

            pos[num] = i

        return -1 if ans == float("inf") else ans