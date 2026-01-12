class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ans = 0
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        i = j = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                ans += 1
                i += 1
                j += 1
            else:
                i += 1
        return ans
