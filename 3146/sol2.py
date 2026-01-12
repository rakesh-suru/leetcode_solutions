class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(i - {ch: j for j, ch in enumerate(t)}[ch]) for i, ch in enumerate(s))