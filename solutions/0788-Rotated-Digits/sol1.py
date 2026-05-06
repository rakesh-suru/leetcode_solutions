class Solution:
    def rotatedDigits(self, n: int) -> int:
        same = {"0", "1", "8"}
        rotate = {"2", "5", "6", "9"}
        invalid = {"3", "4", "7"}
        
        def good(num):
            has_rotate = False
            for dig in str(num):
                if dig in invalid:
                    return False
                if dig in rotate:
                    has_rotate = True
            return has_rotate
        
        ans = 0
        for i in range(1, n + 1):
            if good(i):
                ans += 1
        return ans