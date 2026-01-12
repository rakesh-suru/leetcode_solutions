class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = []
        nums.sort()
        for i in range(len(nums)//2):
            small = nums.pop(0)
            large = nums.pop()
            avg.append((small + large)/2)
        avg.sort()
        return avg[0]
