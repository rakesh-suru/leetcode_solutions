class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = []
        bitmask = 0
        common = 0
        
        for i in range(n):
            a_bit = 1 << (A[i] - 1)
            b_bit = 1 << (B[i] - 1)
            
            if bitmask & a_bit == 0:
                bitmask |= a_bit
            else:
                common += 1
            
            if bitmask & b_bit == 0:
                bitmask |= b_bit
            else:
                common += 1
            
            ans.append(common)
        
        return ans