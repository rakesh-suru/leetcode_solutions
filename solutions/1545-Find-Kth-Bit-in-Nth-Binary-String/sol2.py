class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def solve(n):
            if n == 0:
                return "0"
            
            temp = solve(n-1)
            inv = ""
            for char in temp:
                if char == "0":
                    inv += "1"
                else:
                    inv += "0"

            return temp + "1" + inv[::-1]
        
        return solve(n)[k-1]