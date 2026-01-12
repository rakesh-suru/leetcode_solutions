class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        ans = 0
        for player in sorted(players):
            idx = bisect.bisect_left(trainers, player)
            if idx < len(trainers):
                ans += 1
                trainers.pop(idx)
        return ans
