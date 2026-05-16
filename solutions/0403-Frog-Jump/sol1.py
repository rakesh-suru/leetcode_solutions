class Solution:
    def canCross(self, stones: List[int]) -> bool:

        stone_set = set(stones)

        last = stones[-1]

        def dfs(pos, jump):

            if pos == last:
                return True

            for nxt in [jump - 1, jump, jump + 1]:

                if nxt > 0:

                    next_pos = pos + nxt

                    if next_pos in stone_set:

                        if dfs(next_pos, nxt):
                            return True

            return False

        return dfs(0, 0)