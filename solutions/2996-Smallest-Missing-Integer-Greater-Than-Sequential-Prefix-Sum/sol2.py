class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        temp = set(nums)
        n = len(nums)

        ending = n - 1

        for i in range(1, n):
            if nums[i - 1] + 1 != nums[i]:
                ending = i - 1
                break

        total = 0

        for i in range(ending + 1):
            total += nums[i]

        while total in temp:
            total += 1

        return total