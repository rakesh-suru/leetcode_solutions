class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = left = 0
        right = 1
        for i in range(len(word)-1):
            if word[left] == word[right]:
                ans += 1
            else:
                left = right
            right += 1
        return ans + 1