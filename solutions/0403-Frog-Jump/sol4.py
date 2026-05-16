class Solution:
    def canCross(self, stones: List[int]) -> bool:

        if stones[1] != 1:
            return False

        stone_set = set(stones)

        last = stones[-1]

        memo = {}

        def dfs(pos, jump):

            if pos == last:
                return True

            if (pos, jump) in memo:
                return memo[(pos, jump)]

            for nxt in [jump - 1, jump, jump + 1]:

                if nxt > 0 and pos + nxt in stone_set:

                    if dfs(pos + nxt, nxt):

                        memo[(pos, jump)] = True
                        return True

            memo[(pos, jump)] = False
            return False

        return dfs(1, 1)