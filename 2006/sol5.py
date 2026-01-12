class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        ans = 0
        for num in nums:
            ans += seen[num-k] + seen[num+k]
            seen[num] += 1
        return ans