class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        temp = [0] * (len(gain) + 1)
        alt = 0
        for i in range(len(gain)):
            alt += gain[i]
            temp[i+1] = alt
        return max(temp)