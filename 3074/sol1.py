class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        ans = 0
        capacity.sort(reverse = True)

        for c in capacity:
            if total > 0:
                total -= c
                ans += 1
        
        return ans