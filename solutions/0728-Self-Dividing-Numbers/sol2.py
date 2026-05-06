from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for num in range(left, right + 1):
            temp = str(num)

            if "0" in temp:
                continue
            
            if all(num % int(ch) == 0 for ch in temp):
                ans.append(num)
        
        return ans