class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def check_num(n):
            count = [0] * 10
            s = str(n)
            for d in s:
                count[int(d)] += 1
            
            for d in s:
                if count[int(d)] != int(d):
                    return False
            return True
        
        i = n + 1
        while True:
            if check_num(i):
                return i
            i += 1