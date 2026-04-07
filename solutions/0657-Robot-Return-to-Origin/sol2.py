class Solution:
    def judgeCircle(self, moves: str) -> bool:
        total = 0
        total += moves.count("U")
        total -= moves.count("D")
        total += moves.count("L")
        total -= moves.count("R")

        return total == 0