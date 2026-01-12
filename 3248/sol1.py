class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        ans = 0
        for c in commands:
            if c == "RIGHT":
                ans += 1
            elif c == "LEFT":
                ans -= 1
            elif c == "UP":
                ans -= n
            else:
                ans += n
        return ans