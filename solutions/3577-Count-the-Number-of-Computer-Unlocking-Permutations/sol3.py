from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(complexity)

        if n == 1:
            return 1

        unlocked = complexity[0]
        for i in range(1, n):
            if complexity[i] <= unlocked:
                return 0

        ans = 1
        for x in range(2, n):
            ans = (ans * x) % mod

        return ans
