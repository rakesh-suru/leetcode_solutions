class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        mod =  10**9 + 7

        freq = Counter(nums)
        prev = Counter()

        ans = 0
        prev[nums[0]] += 1

        for i in range(1, n - 1):
            x = nums[i]
            x2 = x << 1
            ans += prev[x2] * (freq[x2] - prev[x2] - (x == 0))
            prev[x] += 1

        return ans % mod
