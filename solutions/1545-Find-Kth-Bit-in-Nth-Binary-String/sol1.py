class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        temp = "0"
        prev = "0"

        for i in range(n):
            inverted = ""

            for char in prev:
                if char == "1":
                    inverted += "0"
                else:
                    inverted += "1"

            temp = prev + "1" + inverted[::-1]
            prev = temp

        return temp[k-1]