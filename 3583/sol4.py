class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        mod = (10 ** 9) + 7
        if n < 3:
            return 0

        rightFreq = Counter(nums)
        leftFreq = defaultdict(int)

        ans = 0

        for j in range(n):
            mid = nums[j]
            rightFreq[mid] -= 1

            target = 2 * mid

            ans += leftFreq[target] * rightFreq[target]

            leftFreq[mid] += 1

        return ans % mod
