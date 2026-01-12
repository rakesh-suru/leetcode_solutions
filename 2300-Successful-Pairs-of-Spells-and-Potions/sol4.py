class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []
        
        for s in spells:
            required = (success + s - 1) // s
            idx = bisect.bisect_left(potions, required)
            ans.append(n - idx)
        return ans
