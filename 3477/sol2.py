class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        total = len(fruits)
        used = [False] * total
        for f in fruits:
            for b in range(len(baskets)):
                if f <= baskets[b] and not used[b]:
                    used[b] = True
                    total -= 1
                    break
        return total