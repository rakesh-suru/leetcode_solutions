class StockSpanner:

    def __init__(self):
        self.prices = []

    def compute_pge(self, prices):
        stack = []
        pge = [-1] * len(prices)

        for i in range(len(prices)):

            while stack and prices[stack[-1]] <= prices[i]:
                stack.pop()

            if stack:
                pge[i] = stack[-1]
            else:
                pge[i] = -1

            stack.append(i)

        return pge

    def next(self, price: int) -> int:
        self.prices.append(price)
        pge = self.compute_pge(self.prices)
        i = len(self.prices) - 1

        if pge[i] == -1:
            return i + 1
        else:
            return i - pge[i]