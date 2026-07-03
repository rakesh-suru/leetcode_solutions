class Solution:
    def processStr(self, s: str) -> str:
        temp = ""

        for char in s:
            if char == "*":
                if temp:
                    temp = temp[:-1]
            elif char == "#":
                temp += temp
            elif char == "%":
                temp = temp[::-1]
            else:
                temp += char
        
        return temp