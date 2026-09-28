class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()

        for p in permutations(digits, 3):
            if p[0] == 0:
                continue

            if p[2] % 2 != 0:
                continue

            num = p[0] * 100 + p[1] * 10 + p[2]
            ans.add(num)

        return len(ans)