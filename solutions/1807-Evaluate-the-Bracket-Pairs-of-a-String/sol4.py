class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapper = dict(knowledge)

        return re.sub(
            r"\((.*?)\)",
            lambda match: mapper.get(match.group(1), "?"),
            s
        )