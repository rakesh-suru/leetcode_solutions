class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt, max_alt = 0, 0
        for g in gain:
            alt += g
            max_alt = max(max_alt, alt)
        return max_alt
