class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        nonzeros = 0
        for x in nums:
            if x > 0:
                nonzeros += 1

        if nonzeros == 0:
            return n * 2
        
        for i in range(n):
            if nums[i] == 0:
                if self.isValid(list(nums), nonzeros, i, -1):
                    count += 1
                if self.isValid(list(nums), nonzeros, i, +1):
                    count += 1
        return count

    def isValid(self, current_nums, nonzeros, start, direction):
        curr = start + direction
        while nonzeros > 0 and 0 <= curr < len(current_nums):
            if current_nums[curr] > 0:
                current_nums[curr] -= 1
                if current_nums[curr] == 0:
                    nonzeros -= 1
                direction *= -1
            curr += direction
        return nonzeros == 0
