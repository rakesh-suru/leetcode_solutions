class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        a_len = len(a)
        b_len = len(b)
        
        temp = a_len - b_len
        if temp > 0:
            b = "0" * temp + b
        else:
            a = "0" * abs(temp) + a
        
        carry = "0"

        for i in range(max(a_len, b_len) -1, -1, -1):
            if carry == "0":
                if a[i] == "0":
                    if b[i] == "0":
                        ans += "0"
                    else:
                        ans += "1"
                else:
                    if b[i] == "0":
                        ans += "1"
                    else:
                        ans += "0"
                        carry = "1"
            
            else:
                if a[i] == "0":
                    if b[i] == "0":
                        ans += "1"
                        carry = "0"
                    else:
                        ans += "0"
                        carry = "1"
                else:
                    if b[i] == "0":
                        ans += "0"
                        carry = "1"
                    else:
                        ans += "1"
                        carry = "1"

        ans += carry if carry == "1" else ""
        return ans[::-1]