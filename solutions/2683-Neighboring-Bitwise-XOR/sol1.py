class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor = derived[0]
        for i in range(1, len(derived)):
            xor ^= derived[i]
        
        return xor == 0