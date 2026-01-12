class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices[:]
        stack = []
        for i,p in enumerate(prices):
            while stack and stack[-1][1] >= p:
                idx, val = stack.pop()
                res[idx] -= p
            stack.append((i, p))
        return res