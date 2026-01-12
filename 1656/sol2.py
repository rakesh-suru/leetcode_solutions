from typing import List

class OrderedStream:
    def __init__(self, n: int):
        self.vals = [""] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        i = idKey - 1
        self.vals[i] = value

        out = []
        while self.ptr < len(self.vals) and self.vals[self.ptr] != "":
            out.append(self.vals[self.ptr])
            self.ptr += 1
        return out


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)