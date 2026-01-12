class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        rem = 0
        for bit in nums:
            rem = (rem * 2 + bit) % 5
            res.append(rem == 0)
        return res
