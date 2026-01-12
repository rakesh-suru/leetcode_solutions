class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []
        
        for s in spells:
            required = (success + s - 1) // s
            left, right = 0, n - 1
            
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] < required:
                    left = mid + 1
                else:
                    right = mid - 1
            
            ans.append(n - left)
        return ans
