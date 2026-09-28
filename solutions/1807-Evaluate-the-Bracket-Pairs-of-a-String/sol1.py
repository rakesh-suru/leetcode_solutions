class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len(s)
        left = 0
        right = 0
        ans = ""

        while right < n:
            if s[right] == "(":
                left = right
                right += 1
                temp = ""

                while s[right] != ")":
                    temp += s[right]
                    right += 1

                to_add = "?"
                for key, val in knowledge:
                    if temp == key:
                        to_add = val
                
                ans += to_add
            
            else:
                ans += s[right]
            
            right += 1
        
        return ans