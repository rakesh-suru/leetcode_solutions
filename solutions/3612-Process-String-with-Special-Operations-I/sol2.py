class Solution:
    def processStr(self, s: str) -> str:
        temp = []

        for char in s:
            if char == "*":
                if temp:
                    temp.pop()
            elif char == "#":
                temp.extend(temp)
            elif char == "%":
                temp.reverse()
            else:
                temp.append(char)
        
        return "".join(temp)