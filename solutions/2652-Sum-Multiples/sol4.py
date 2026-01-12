class Solution:
    def sumOfMultiples(self, n: int) -> int:
        nums = set()
        for x in [3, 5, 7]:
            nums.update(range(x, n+1, x))
        return sum(nums)
