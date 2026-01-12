class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hashmap = {ch : i for i, ch in enumerate(t)}
        ans = 0
        for i, ch in enumerate(s):
            ans += abs(i - hashmap[ch])
        return ans