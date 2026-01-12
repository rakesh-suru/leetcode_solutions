class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = Counter(num % value for num in nums)
        i = 0
        while count[i % value] > i // value:
            i += 1
        return i
