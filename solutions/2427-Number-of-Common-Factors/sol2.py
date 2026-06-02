class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        set1 = set()
        set2 = set()

        for i in range(1, a + 1):
            if a % i == 0:
                set1.add(i)
        
        for i in range(1, b + 1):
            if b % i == 0:
                set2.add(i)
        
        set1 = set1.intersection(set2)
        return len(set1)