class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = []
        low = 0
        high = len(s)

        for i in s:
            if i == "I":
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
        ans.append(low)
        return ans