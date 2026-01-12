class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        mod = 10 ** 9 + 7
        if n < 3:
            return 0

        rightFreq = Counter(nums)
        leftFreq = defaultdict(int)

        for j in range(n):
            mid = nums[j]
            rightFreq[mid] -= 1

            target = 2 * mid
            leftCount = leftFreq[target]
            rightCount = rightFreq[target]

            ans += leftCount * rightCount
            leftFreq[mid] += 1

        return ans % mod