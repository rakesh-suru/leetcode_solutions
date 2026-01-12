class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_pos = {ch: i for i, ch in enumerate(s)}
        t_pos = {ch: i for i, ch in enumerate(t)}
        return sum(abs(s_pos[ch] - t_pos[ch]) for ch in s)