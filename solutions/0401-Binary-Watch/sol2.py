from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        leds = [8,4,2,1,32,16,8,4,2,1]
        
        def backtrack(index, count, hrs, mins):
            if hrs > 11 or mins > 59:
                return
            
            if count == 0:
                ans.append(f"{hrs}:{mins:02d}")
                return
            
            for i in range(index, len(leds)):
                if i < 4:
                    backtrack(i+1, count-1, hrs+leds[i], mins)
                else:
                    backtrack(i+1, count-1, hrs, mins+leds[i])
        
        backtrack(0, turnedOn, 0, 0)
        return ans
