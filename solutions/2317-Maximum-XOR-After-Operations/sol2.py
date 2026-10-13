class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        return reduce(lambda a, b: a | b, nums)