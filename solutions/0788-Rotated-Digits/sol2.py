class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid = {'3','4','7'}
        rotate = {'2','5','6','9'}
        
        def good(x):
            changed = False
            for d in str(x):
                if d in invalid:
                    return False
                if d in rotate:
                    changed = True
            return changed
        
        return sum(good(i) for i in range(1, n+1))