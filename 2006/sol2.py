from collections import Counter

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        ans = 0
        for num in count:
            ans += count[num] * count.get(num + k, 0)
        return ans
