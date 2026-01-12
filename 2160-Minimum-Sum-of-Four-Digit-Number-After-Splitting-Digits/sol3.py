from itertools import permutations

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = list(str(num))
        min_sum = float('inf')
        
        for p in permutations(digits):
            num1 = int(p[0] + p[1])
            num2 = int(p[2] + p[3])
            min_sum = min(min_sum, num1 + num2)
        
        return min_sum
