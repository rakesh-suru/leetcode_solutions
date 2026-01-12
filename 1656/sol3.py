class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.ptr = 1
        self.map: Dict[int, str] = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.map[idKey] = value
        out = []
        while self.ptr in self.map:
            out.append(self.map[self.ptr])
            self.ptr += 1
        return out


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)