class Solution:
    def decompressRLElist(self, N: List[int]) -> List[int]:
        return sum([N[i]*[N[i+1]] for i in range(0,len(N),2)],[])