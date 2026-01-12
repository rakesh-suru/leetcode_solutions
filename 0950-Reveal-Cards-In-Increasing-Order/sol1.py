class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        ans = [0] * n
        queue = deque(range(n))

        for num in deck:
            idx = queue.popleft()
            ans[idx] = num
            
            if queue:
                idx = queue.popleft()
                queue.append(idx)

        return ans
