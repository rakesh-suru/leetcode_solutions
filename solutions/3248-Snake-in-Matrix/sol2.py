class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        move = {
            "RIGHT": 1,
            "LEFT": -1,
            "UP": -n,
            "DOWN": n
        }
        ans = 0
        for c in commands:
            ans += move[c]
        return ans
