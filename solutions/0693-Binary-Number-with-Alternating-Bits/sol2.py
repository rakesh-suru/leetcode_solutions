class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = bin(n)[2:]
        if abs(num.count("1") - num.count("0")) not in [0, 1]:
            return False
        
        for i in range(len(num) - 1):
            if num[i] == num[i + 1]:
                return False
        return True