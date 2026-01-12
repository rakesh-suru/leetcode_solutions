class OrderedStream:

    def __init__(self, n: int):
        self.temp = [""] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.temp[idKey - 1] = value
        
        res = []
        while self.ptr < len(self.temp) and self.temp[self.ptr] != "":
            res.append(self.temp[self.ptr])
            self.ptr += 1
        
        return res



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)