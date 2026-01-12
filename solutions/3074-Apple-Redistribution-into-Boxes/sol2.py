class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)

        used = 0
        for c in capacity:
            total -= c
            used += 1
            if total <= 0:
                return used
