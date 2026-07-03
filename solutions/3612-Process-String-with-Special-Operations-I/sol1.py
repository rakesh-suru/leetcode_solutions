class Solution:
    def processStr(self, s: str) -> str:
        temp = []

        for char in s:
            if char == "*":
                if temp:
                    temp.pop()
            elif char == "#":
                temp = temp + temp
            elif char == "%":
                temp = temp[::-1]
            else:
                temp.append(char)
        
        return "".join(temp)