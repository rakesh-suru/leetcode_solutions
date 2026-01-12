class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        dup = set()
        for n in nums:
            if n in seen:
                dup.add(n)
            else:
                seen.add(n)
        return list(dup)
