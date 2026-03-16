class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:

        if not self.stack:
            self.stack.append(val)
            self.mini = val

        elif val >= self.mini:
            self.stack.append(val)

        else:
            encoded = 2*val - self.mini
            self.stack.append(encoded)
            self.mini = val


    def pop(self) -> None:

        if not self.stack:
            return

        top = self.stack.pop()

        if top < self.mini:
            self.mini = 2*self.mini - top


    def top(self) -> int:

        top = self.stack[-1]

        if top < self.mini:
            return self.mini

        return top


    def getMin(self) -> int:
        return self.mini