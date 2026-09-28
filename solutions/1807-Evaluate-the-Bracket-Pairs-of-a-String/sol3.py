class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapper = dict(knowledge)

        ans = ""
        right = 0

        while right < len(s):
            if s[right] == "(":
                start = right + 1
                right += 1

                while s[right] != ")":
                    right += 1

                key = s[start:right]
                ans += mapper.get(key, "?")

            else:
                ans += s[right]

            right += 1

        return ans