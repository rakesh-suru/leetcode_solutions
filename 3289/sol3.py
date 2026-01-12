class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicates = []
        for n in nums:
            if n in seen and n not in duplicates:
                duplicates.append(n)
            seen.add(n)
        return duplicates
