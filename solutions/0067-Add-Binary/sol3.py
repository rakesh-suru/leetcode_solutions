class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        carry = 0
        
        for i in range(max_len - 1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry
            
            ans += str(total % 2)
            carry = total // 2
        
        if carry:
            ans += "1"
        
        return ans[::-1]
