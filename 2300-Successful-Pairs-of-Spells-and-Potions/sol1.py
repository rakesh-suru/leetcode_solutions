class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        for i in spells:
            temp = 0
            for j in potions:
                if i * j >= success:
                    temp += 1
            ans.append(temp)
        return ans