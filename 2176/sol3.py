from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)

        ans = 0
        for indices in index_map.values():
            for i in range(len(indices)):
                for j in range(i+1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        ans += 1
        return ans
