class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = homepage
        self.forwardStack = []
        self.backStack = []

    def visit(self, url: str) -> None:
        self.backStack.append(self.curr)
        self.curr = url
        self.forwardStack = []

    def back(self, steps: int) -> str:
        while steps > 0 and self.backStack:
            self.forwardStack.append(self.curr)
            self.curr = self.backStack.pop()
            steps -= 1
        return self.curr

    def forward(self, steps: int) -> str:
        while steps > 0 and self.forwardStack:
            self.backStack.append(self.curr)
            self.curr = self.forwardStack.pop()
            steps -= 1
        return self.curr


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)