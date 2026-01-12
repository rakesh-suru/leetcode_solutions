class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        exists = [False] * 201
        for num in nums:
            exists[num] = True
        count = 0
        for num in nums:
            if num + diff < 201 and num + 2 * diff < 201:
                if exists[num + diff] and exists[num + 2 * diff]:
                    count += 1
        return count
