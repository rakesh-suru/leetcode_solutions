class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        size = len(nums[0])
        nums_set = set(nums)

        for i in range(0, 2 ** size):
            b = bin(i)[2:].zfill(size)
            if b not in nums_set:
                return b