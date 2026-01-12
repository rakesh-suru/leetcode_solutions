class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        idx_map = [0] * 26
        for i in range(len(t)):
            idx_map[ord(t[i]) - ord('a')] = i
        return sum(abs(i - idx_map[ord(s[i]) - ord('a')]) for i in range(len(s)))
