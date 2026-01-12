class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seats = []
        for index, seat in enumerate(corridor):
            if seat == "S":
                seats.append(index)
        
        l = len(seats)
        if l < 2 or l % 2 == 1:
            return 0
        
        res = 1
        i = 1
        while i < l - 1:
            res = (res * (seats[i+1] - seats[i])) % MOD
            i += 2
        
        return res