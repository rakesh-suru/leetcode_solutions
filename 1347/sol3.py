class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        for ch in t:
            freq[ord(ch) - 97] -= 1
        return sum(x for x in freq if x > 0)