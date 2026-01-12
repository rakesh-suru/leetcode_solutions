class Solution:
    def convertDateToBinary(self, date: str) -> str:
        temp = date.split("-")
        temp = map(lambda x : bin(int(x))[2:], temp)

        return "-".join(temp)