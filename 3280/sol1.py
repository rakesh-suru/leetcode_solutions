class Solution:
    def convertDateToBinary(self, date: str) -> str:
        temp = date.split("-")
        binary = [str(bin(int(i))[2:]) for i in temp]

        return "-".join(binary)