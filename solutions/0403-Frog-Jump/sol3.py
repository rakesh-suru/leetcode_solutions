class Solution:
    def canCross(self, stones: List[int]) -> bool:

        n = len(stones)
        mapper = {}

        for i in range(n):
            mapper[stones[i]] = i

        dp = [set() for _ in range(n)]

        dp[0].add(0)

        for i in range(n):

            for jump in dp[i]:

                for nxt in [jump - 1, jump, jump + 1]:

                    if nxt > 0:

                        next_pos = stones[i] + nxt

                        if next_pos in mapper:

                            idx = mapper[next_pos]

                            dp[idx].add(nxt)

        return len(dp[-1]) > 0