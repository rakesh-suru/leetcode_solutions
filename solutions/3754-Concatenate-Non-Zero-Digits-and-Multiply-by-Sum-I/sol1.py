class Solution:
    def sumAndMultiply(self, n: int) -> int:
        temp = list(str(n))
        total = sum(int(i) for i in temp)
        new_num = 0

        for i in temp:
            if i != "0":
                new_num = new_num * 10 + int(i)
            
        return new_num * total