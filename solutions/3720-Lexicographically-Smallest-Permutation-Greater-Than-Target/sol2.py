class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        import itertools

        temp = list(s)

        perms = list(itertools.permutations(temp))
        perms.sort()

        for perm in perms:
            if perm > tuple(target):
                return "".join(perm)

        return ""