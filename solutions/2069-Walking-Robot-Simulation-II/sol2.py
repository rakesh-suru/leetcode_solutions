class Robot:

    def __init__(self, width: int, height: int):
        self.max_w = width
        self.max_h = height
        self.curr = [0, 0]
        self.dir = 0

    def step(self, num: int) -> None:
        if self.max_w == 1 or self.max_h == 1:
            return

        perimeter = 2 * (self.max_w + self.max_h) - 4
        num %= perimeter
        if num == 0:
            num = perimeter

        while num > 0:
            if self.dir == 0:
                steps = min(num, self.max_w - 1 - self.curr[0])
                self.curr[0] += steps
            elif self.dir == 1:
                steps = min(num, self.max_h - 1 - self.curr[1])
                self.curr[1] += steps
            elif self.dir == 2:
                steps = min(num, self.curr[0])
                self.curr[0] -= steps
            else:
                steps = min(num, self.curr[1])
                self.curr[1] -= steps

            num -= steps
            if num > 0:
                self.dir = (self.dir + 1) % 4

    def getPos(self) -> List[int]:
        return self.curr

    def getDir(self) -> str:
        return ["East", "North", "West", "South"][self.dir]