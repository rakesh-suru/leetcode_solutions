class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cnt = 1
        
        i = len(self.stack) - 1
        
        while i >= 0:
            if self.stack[i] > price:
                break
            cnt += 1
            i -= 1
        
        self.stack.append(price)
        return cnt