class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        temp = [0] * (len(gain) + 1)
        alt = 0
        for i in range(len(gain)):
            temp[i+1] = alt + gain[i]
            alt += gain[i]
        return max(temp)