class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        cnt = Counter(commands)
        return (cnt["RIGHT"] - cnt["LEFT"]
            + n * (cnt["DOWN"] - cnt["UP"])
        )
