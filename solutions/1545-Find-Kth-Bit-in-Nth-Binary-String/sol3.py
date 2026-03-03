class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev = "0"

        for _ in range(1, n):
            inverted = ""

            for char in prev:
                if char == "1":
                    inverted += "0"
                else:
                    inverted += "1"

            prev = prev + "1" + inverted[::-1]

        return prev[k-1]