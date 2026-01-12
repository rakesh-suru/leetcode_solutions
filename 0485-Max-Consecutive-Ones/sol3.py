class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(len(s) for s in ''.join(map(str, nums)).split('0'))
