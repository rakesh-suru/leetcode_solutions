class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for j in range(n):
            mid = nums[j]
            target = 2 * mid

            leftCount = 0
            for i in range(j):
                if nums[i] == target:
                    leftCount += 1

            rightCount = 0
            for k in range(j + 1, n):
                if nums[k] == target:
                    rightCount += 1

            ans += leftCount * rightCount

        return ans