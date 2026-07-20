class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        for num in range(low, high + 1):
            s = str(num)
            valid = True

            for i in range(len(s) - 1):
                if int(s[i + 1]) - int(s[i]) != 1:
                    valid = False
                    break

            if valid:
                ans.append(num)

        return ans