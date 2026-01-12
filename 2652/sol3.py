class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0 or x % 7 == 0, range(3, n+1)))
