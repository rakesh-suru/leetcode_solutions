class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0

        for i in range(31, -1, -1):
            mask |= (1 << i)

            seen = set()

            for num in nums:
                seen.add(num & mask)

            temp = ans | (1 << i)

            if any((temp ^ x) in seen for x in seen):
                ans = temp

        return ans