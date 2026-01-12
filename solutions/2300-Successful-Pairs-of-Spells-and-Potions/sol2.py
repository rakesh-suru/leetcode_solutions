class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = [0] * len(spells)
        n = len(potions)
        for i in range(len(spells)):
            for j in range(len(potions)):
                if spells[i] * potions[j] >= success:
                    ans[i] = n - j
                    break

        return ans