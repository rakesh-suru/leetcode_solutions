from collections import defaultdict

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        prefixXor = 0
        count = defaultdict(int)
        total = defaultdict(int)
        count[0] = 1  # prefixXor 0 at index -1
        total[0] = -1

        for i, val in enumerate(arr):
            prefixXor ^= val
            if prefixXor in count:
                ans += count[prefixXor] * i - total[prefixXor] - count[prefixXor]
            count[prefixXor] += 1
            total[prefixXor] += i
        return ans
