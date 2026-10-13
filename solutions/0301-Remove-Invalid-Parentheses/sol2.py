class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def is_valid(s):
            cnt = 0

            for ch in s:
                if ch == "(":
                    cnt += 1
                elif ch == ")":
                    cnt -= 1

                    if cnt < 0:
                        return False

            return cnt == 0

        level = {s}

        while level:
            valid = []

            for st in level:
                if is_valid(st):
                    valid.append(st)

            if valid:
                return valid

            next_level = set()

            for st in level:
                for i in range(len(st)):
                    if st[i] in "()":
                        next_level.add(st[:i] + st[i + 1:])

            level = next_level

        return [""]