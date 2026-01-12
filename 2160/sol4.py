class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        result = []
        for _ in range(4):
            min_val = min(digits)
            result.append(min_val)
            digits.remove(min_val)
        
        num1 = result[0] * 10 + result[2]
        num2 = result[1] * 10 + result[3]
        return num1 + num2
