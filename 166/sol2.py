class Solution:
    def fractionToDecimal(self, num: int, den: int) -> str:
        if den == 0:
            return ""
        if den == 1 or num == 0:
            return f"{num}"
        if num % den == 0:
            return f"{num // den}"
        
        res = ""
        if (num < 0) ^ (den < 0):
            res += "-"
        num, den = abs(num), abs(den)
        quotient, rem = divmod(num, den)
        res += str(quotient) + "."
        repeat = {}
        while rem:
            if rem in repeat:
                ind = repeat[rem]
                return ''.join(res[:ind]) + '(' + ''.join(res[ind:]) + ')'
            repeat[rem] = len(res)
            quotient, rem = divmod(rem * 10, den)
            res += str(quotient)
            
        return res