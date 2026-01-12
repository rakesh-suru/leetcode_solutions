class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 0:
            return []
        dp = ["0", "1"]
        for i in range(1, n):
            temp = []
            for s in dp:
                temp.append(s + "1")
                if s[-1] == "1":
                    temp.append(s + "0")
            dp = temp
        return dp