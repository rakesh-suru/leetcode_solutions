class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len(s)
        right = 0
        ans = ""
        mapper = dict(knowledge)

        while right < n:
            if s[right] == "(":
                right += 1
                temp = ""

                while s[right] != ")":
                    temp += s[right]
                    right += 1
                
                ans += mapper.get(temp, "?")
            
            else:
                ans += s[right]
            
            right += 1
        
        return ans