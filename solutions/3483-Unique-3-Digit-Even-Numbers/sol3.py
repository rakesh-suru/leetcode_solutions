class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()
        n = len(digits)

        def backtrack(path, used):
            if len(path) == 3:
                if path[-1] % 2 == 0:
                    num = path[0] * 100 + path[1] * 10 + path[2]
                    ans.add(num)
                return

            for i in range(n):
                if used[i]:
                    continue

                if len(path) == 0 and digits[i] == 0:
                    continue

                used[i] = True
                path.append(digits[i])

                backtrack(path, used)

                path.pop()
                used[i] = False

        backtrack([], [False] * n)

        return len(ans)