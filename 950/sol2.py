class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        ans = [0] * n
        temp = list(range(n))

        for num in deck:
            idx = temp.pop(0)
            ans[idx] = num
            
            if temp:
                idx = temp.pop(0)
                temp.append(idx)

        return ans
