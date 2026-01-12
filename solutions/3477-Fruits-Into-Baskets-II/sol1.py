class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        temp = [0 for i in fruits]
        total = len(fruits)
        for f in fruits:
            for b in range(len(baskets)):
                if f <= baskets[b] and temp[b] == 0:
                    temp[b] = 1
                    total -= 1
                    break
        return total